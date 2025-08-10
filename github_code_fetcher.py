#!/usr/bin/env python3
"""
GitHub Code Fetcher

A Python tool that searches GitHub for repositories related to a specific topic
and automatically downloads the top repositories to your computer.

Features:
- Keyword-based search
- Sorting options (stars, recent, best match)
- Automatic download (clone or ZIP)
- Metadata storage to CSV
- Language and star count filters

Author: Sreeram (sreeram.lagisetty@gmail.com)
GitHub: https://github.com/Sreeram5678
Repository: https://github.com/Sreeram5678/GITHUB-Code-Fetcher.git
"""

import os
import sys
import csv
import json
import zipfile
import requests
import re
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional
from urllib.parse import urljoin
import click
import pandas as pd
from tqdm import tqdm
import git
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def sanitize_folder_name(query: str, language: str = None, min_stars: int = 0) -> str:
    """Create a safe folder name from the search query and filters.
    
    Args:
        query: Original search query
        language: Programming language filter
        min_stars: Minimum star count filter
        
    Returns:
        Sanitized folder name
    """
    # Remove special characters and replace spaces with underscores
    folder_name = re.sub(r'[<>:"/\\|?*]', '', query)
    folder_name = re.sub(r'\s+', '_', folder_name.strip())
    
    # Add language suffix if specified
    if language:
        folder_name += f"_{language}"
    
    # Add star filter suffix if specified
    if min_stars > 0:
        folder_name += f"_min{min_stars}stars"
    
    # Limit length and ensure it's not empty
    folder_name = folder_name[:50]  # Limit to 50 characters
    if not folder_name:
        folder_name = "search_results"
    
    return folder_name

class GitHubCodeFetcher:
    """Main class for GitHub repository search and download functionality."""
    
    def __init__(self, token: Optional[str] = None):
        """Initialize the GitHub Code Fetcher.
        
        Args:
            token: GitHub personal access token for authenticated requests
        """
        self.token = token or os.getenv('GITHUB_TOKEN')
        self.base_url = "https://api.github.com"
        self.session = requests.Session()
        
        if self.token:
            self.session.headers.update({
                'Authorization': f'token {self.token}',
                'Accept': 'application/vnd.github.v3+json'
            })
        else:
            click.echo("Warning: No GitHub token provided. API rate limits will be lower.")
            
    def search_repositories(
        self,
        query: str,
        sort: str = "stars",
        order: str = "desc",
        language: Optional[str] = None,
        min_stars: int = 0,
        max_results: int = 10,
        per_page: int = 30
    ) -> List[Dict]:
        """Search GitHub repositories based on query and filters.
        
        Args:
            query: Search query string
            sort: Sort by 'stars', 'updated', or 'best-match'
            order: 'asc' or 'desc'
            language: Programming language filter
            min_stars: Minimum star count
            max_results: Maximum number of results to return
            per_page: Results per API page (max 100)
            
        Returns:
            List of repository dictionaries
        """
        search_query = query
        
        # Add language filter to query
        if language:
            search_query += f" language:{language}"
            
        # Add star filter to query
        if min_stars > 0:
            search_query += f" stars:>={min_stars}"
            
        params = {
            'q': search_query,
            'sort': sort,
            'order': order,
            'per_page': min(per_page, 100)
        }
        
        repositories = []
        page = 1
        
        with tqdm(desc="Searching repositories", unit="repos") as pbar:
            while len(repositories) < max_results:
                params['page'] = page
                
                try:
                    response = self.session.get(
                        f"{self.base_url}/search/repositories",
                        params=params
                    )
                    response.raise_for_status()
                    
                    data = response.json()
                    items = data.get('items', [])
                    
                    if not items:
                        break
                        
                    for repo in items:
                        if len(repositories) >= max_results:
                            break
                            
                        repo_data = {
                            'name': repo['name'],
                            'full_name': repo['full_name'],
                            'description': repo.get('description', ''),
                            'html_url': repo['html_url'],
                            'clone_url': repo['clone_url'],
                            'stars': repo['stargazers_count'],
                            'forks': repo['forks_count'],
                            'language': repo.get('language', ''),
                            'size': repo['size'],
                            'created_at': repo['created_at'],
                            'updated_at': repo['updated_at'],
                            'topics': repo.get('topics', []),
                            'license': repo.get('license', {}).get('name', '') if repo.get('license') else '',
                            'archived': repo.get('archived', False),
                            'default_branch': repo.get('default_branch', 'main')
                        }
                        repositories.append(repo_data)
                        pbar.update(1)
                        
                    page += 1
                    
                    # Check if we've reached the last page
                    if page > (data.get('total_count', 0) // per_page) + 1:
                        break
                        
                except requests.exceptions.RequestException as e:
                    click.echo(f"Error searching repositories: {e}")
                    break
                    
        return repositories[:max_results]
    
    def download_repository(
        self,
        repo_data: Dict,
        download_dir: str = "downloaded_repos",
        method: str = "clone"
    ) -> bool:
        """Download a repository either by cloning or downloading ZIP.
        
        Args:
            repo_data: Repository information dictionary
            download_dir: Directory to download repositories to
            method: 'clone' or 'zip'
            
        Returns:
            Success status
        """
        repo_name = repo_data['full_name'].replace('/', '_')
        repo_path = Path(download_dir) / repo_name
        
        # Create download directory if it doesn't exist
        Path(download_dir).mkdir(exist_ok=True)
        
        # Skip if already exists
        if repo_path.exists():
            click.echo(f"Repository {repo_name} already exists, skipping...")
            return True
            
        try:
            if method == "clone":
                return self._clone_repository(repo_data, repo_path)
            else:
                return self._download_zip(repo_data, repo_path)
                
        except Exception as e:
            click.echo(f"Error downloading {repo_name}: {e}")
            return False
    
    def _clone_repository(self, repo_data: Dict, repo_path: Path) -> bool:
        """Clone repository using git."""
        try:
            click.echo(f"Cloning {repo_data['full_name']}...")
            git.Repo.clone_from(repo_data['clone_url'], repo_path)
            return True
        except git.exc.GitError as e:
            click.echo(f"Git clone failed for {repo_data['full_name']}: {e}")
            return False
    
    def _download_zip(self, repo_data: Dict, repo_path: Path) -> bool:
        """Download repository as ZIP file and extract."""
        try:
            # GitHub ZIP download URL
            zip_url = f"https://github.com/{repo_data['full_name']}/archive/refs/heads/{repo_data['default_branch']}.zip"
            
            click.echo(f"Downloading ZIP for {repo_data['full_name']}...")
            
            response = self.session.get(zip_url, stream=True)
            response.raise_for_status()
            
            # Download ZIP file
            zip_path = repo_path.with_suffix('.zip')
            total_size = int(response.headers.get('content-length', 0))
            
            with open(zip_path, 'wb') as f:
                with tqdm(total=total_size, unit='B', unit_scale=True, desc=f"Downloading {repo_data['name']}") as pbar:
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
                            pbar.update(len(chunk))
            
            # Extract ZIP file
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(repo_path.parent)
                
            # Rename extracted folder to remove branch suffix
            extracted_folder = repo_path.parent / f"{repo_data['name']}-{repo_data['default_branch']}"
            if extracted_folder.exists():
                extracted_folder.rename(repo_path)
            
            # Remove ZIP file
            zip_path.unlink()
            
            return True
            
        except Exception as e:
            click.echo(f"ZIP download failed for {repo_data['full_name']}: {e}")
            return False
    
    def save_metadata(self, repositories: List[Dict], filename: str = "repository_metadata.csv") -> None:
        """Save repository metadata to CSV file.
        
        Args:
            repositories: List of repository dictionaries
            filename: Output CSV filename
        """
        if not repositories:
            click.echo("No repositories to save.")
            return
            
        # Convert to DataFrame for easy CSV export
        df = pd.DataFrame(repositories)
        
        # Add download timestamp
        df['downloaded_at'] = datetime.now().isoformat()
        
        # Reorder columns for better readability
        column_order = [
            'name', 'full_name', 'description', 'stars', 'forks', 'language',
            'html_url', 'clone_url', 'size', 'created_at', 'updated_at',
            'topics', 'license', 'archived', 'default_branch', 'downloaded_at'
        ]
        
        df = df.reindex(columns=column_order)
        
        # Save to CSV
        df.to_csv(filename, index=False)
        click.echo(f"Metadata saved to {filename}")

@click.command()
@click.option('--query', '-q', required=True, help='Search query for repositories')
@click.option('--max-results', '-n', default=10, help='Maximum number of repositories to fetch')
@click.option('--sort', '-s', 
              type=click.Choice(['stars', 'updated', 'best-match']), 
              default='stars', 
              help='Sort repositories by')
@click.option('--order', '-o', 
              type=click.Choice(['asc', 'desc']), 
              default='desc', 
              help='Sort order')
@click.option('--language', '-l', help='Filter by programming language')
@click.option('--min-stars', default=0, help='Minimum star count')
@click.option('--download-dir', '-d', default='downloaded_repos', help='Download directory')
@click.option('--method', '-m', 
              type=click.Choice(['clone', 'zip']), 
              default='clone', 
              help='Download method')
@click.option('--metadata-file', default='repository_metadata.csv', help='Metadata CSV filename')
@click.option('--token', help='GitHub personal access token')
@click.option('--search-only', is_flag=True, help='Only search, do not download')
def main(query, max_results, sort, order, language, min_stars, download_dir, 
         method, metadata_file, token, search_only):
    """GitHub Code Fetcher - Search and download GitHub repositories by topic."""
    
    click.echo(f"GitHub Code Fetcher")
    click.echo(f"==================")
    click.echo(f"Query: {query}")
    click.echo(f"Max results: {max_results}")
    click.echo(f"Sort by: {sort} ({order})")
    if language:
        click.echo(f"Language: {language}")
    if min_stars > 0:
        click.echo(f"Min stars: {min_stars}")
    click.echo()
    
    # Initialize fetcher
    fetcher = GitHubCodeFetcher(token=token)
    
    # Search repositories
    click.echo("Searching repositories...")
    repositories = fetcher.search_repositories(
        query=query,
        sort=sort,
        order=order,
        language=language,
        min_stars=min_stars,
        max_results=max_results
    )
    
    if not repositories:
        click.echo("No repositories found matching your criteria.")
        return
    
    click.echo(f"\nFound {len(repositories)} repositories:")
    for i, repo in enumerate(repositories, 1):
        click.echo(f"{i:2d}. {repo['full_name']} ⭐{repo['stars']} ({repo['language']})")
        click.echo(f"    {repo['description'][:80]}..." if len(repo['description']) > 80 else f"    {repo['description']}")
    
    # Create topic-based folder name
    topic_folder = sanitize_folder_name(query, language, min_stars)
    topic_download_dir = Path(download_dir) / topic_folder
    
    # Create metadata directory and filename
    metadata_dir = Path("metadata")
    metadata_dir.mkdir(exist_ok=True)
    topic_metadata_file = metadata_dir / f"{topic_folder}_{metadata_file}"
    
    # Save metadata
    fetcher.save_metadata(repositories, str(topic_metadata_file))
    
    if search_only:
        click.echo(f"\nSearch completed. Metadata saved to '{topic_metadata_file}'")
        click.echo("Use --search-only=false to download repositories.")
        return
    
    # Download repositories
    click.echo(f"\nDownloading repositories to '{topic_download_dir}'...")
    success_count = 0
    
    for repo in tqdm(repositories, desc="Downloading repositories"):
        if fetcher.download_repository(repo, str(topic_download_dir), method):
            success_count += 1
    
    click.echo(f"\nDownload completed!")
    click.echo(f"Successfully downloaded: {success_count}/{len(repositories)} repositories")
    click.echo(f"Download directory: {topic_download_dir}")
    click.echo(f"Metadata file: {topic_metadata_file}")
    click.echo(f"Topic folder: {topic_folder}")

if __name__ == "__main__":
    main()
