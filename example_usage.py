#!/usr/bin/env python3
"""
Example usage of GitHub Code Fetcher

This script demonstrates how to use the GitHubCodeFetcher class
programmatically in your own Python scripts.

Author: Sreeram (sreeram.lagisetty@gmail.com)
GitHub: https://github.com/Sreeram5678
Repository: https://github.com/Sreeram5678/GITHUB-Code-Fetcher.git
"""

from github_code_fetcher import GitHubCodeFetcher
import os

def main():
    """Example usage of GitHub Code Fetcher."""
    
    # Initialize the fetcher (will use GITHUB_TOKEN from .env if available)
    fetcher = GitHubCodeFetcher()
    
    # Example 1: Search for machine learning repositories
    print("Example 1: Searching for machine learning repositories...")
    ml_repos = fetcher.search_repositories(
        query="machine learning",
        language="python",
        min_stars=100,
        max_results=5,
        sort="stars"
    )
    
    print(f"Found {len(ml_repos)} repositories:")
    for repo in ml_repos:
        print(f"- {repo['full_name']} ⭐{repo['stars']} - {repo['description'][:60]}...")
    
    # Save metadata
    fetcher.save_metadata(ml_repos, "ml_repos_metadata.csv")
    
    # Example 2: Download repositories
    print("\nExample 2: Downloading first repository...")
    if ml_repos:
        success = fetcher.download_repository(
            ml_repos[0], 
            download_dir="example_downloads",
            method="zip"  # Use ZIP for faster download
        )
        print(f"Download {'successful' if success else 'failed'}")
    
    # Example 3: Search for recent JavaScript projects
    print("\nExample 3: Searching for recent JavaScript projects...")
    js_repos = fetcher.search_repositories(
        query="react components",
        language="javascript",
        sort="updated",
        max_results=3
    )
    
    for repo in js_repos:
        print(f"- {repo['full_name']} (updated: {repo['updated_at'][:10]})")

if __name__ == "__main__":
    main()
