# GitHub Code Fetcher

A powerful Python tool that searches GitHub for repositories related to specific topics and automatically downloads them to your computer. Perfect for researchers, developers, and anyone who wants to quickly find and collect working codebases for study, experimentation, or integration.

## Author

- **Name**: Sreeram
- **Email**: sreeram.lagisetty@gmail.com
- **GitHub**: [@Sreeram5678](https://github.com/Sreeram5678)
- **Instagram**: [@sreeram_3012](https://www.instagram.com/sreeram_3012?igsh=N2Fub3A5eWF4cjJs&utm_source=qr)

## Repository

This project is hosted at: [https://github.com/Sreeram5678/GITHUB-Code-Fetcher.git](https://github.com/Sreeram5678/GITHUB-Code-Fetcher.git)

## Status

![CI](https://github.com/Sreeram5678/GITHUB-Code-Fetcher/workflows/CI/badge.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)

## Features

- **Keyword-based search**: Find repositories by topic, technology, or any search term
- **Flexible sorting**: Sort by stars, most recent updates, or best match
- **Automatic download**: Clone repositories with Git or download as ZIP files
- **Smart organization**: Automatically creates topic-based folders for organized storage
- **Metadata storage**: Save repository details to CSV for easy reference and analysis
- **Advanced filters**: Filter by programming language, minimum star count, and more
- **Progress tracking**: Visual progress bars for search and download operations
- **Rate limit handling**: Supports GitHub personal access tokens for higher API limits

## Installation

1. **Clone or download this repository**
2. **Create and activate virtual environment**:
   ```bash
   python3 -m venv code_fetcher
   source code_fetcher/bin/activate  # On Windows: code_fetcher\Scripts\activate
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration (Optional but Recommended)

For higher API rate limits, create a GitHub personal access token:

1. Go to [GitHub Settings > Personal Access Tokens](https://github.com/settings/tokens)
2. Click "Generate new token (classic)"
3. Select "public_repo" scope for public repositories
4. Copy the generated token
5. Create a `.env` file in the project directory:
   ```bash
   cp config_example.env .env
   ```
6. Edit `.env` and add your token:
   ```
   GITHUB_TOKEN=your_actual_token_here
   ```

## Usage

### Basic Usage

```bash
# Search and download top 10 repositories about machine learning
python github_code_fetcher.py -q "machine learning" -n 10

# Search for Python repositories about neural networks
python github_code_fetcher.py -q "neural networks" -l python -n 5

# Search for high-quality repositories (minimum 100 stars)
python github_code_fetcher.py -q "react components" --min-stars 100 -n 15
```

### Advanced Usage

```bash
# Sort by most recently updated
python github_code_fetcher.py -q "kubernetes" -s updated -n 20

# Download as ZIP files instead of cloning
python github_code_fetcher.py -q "tensorflow" -m zip -n 10

# Search only (don't download)
python github_code_fetcher.py -q "blockchain" --search-only

# Custom download directory and metadata file
python github_code_fetcher.py -q "pytorch" -d ./ai_repos -n 15 --metadata-file ai_metadata.csv
```

### Command Line Options

| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| `--query` | `-q` | Search query for repositories | Required |
| `--max-results` | `-n` | Maximum number of repositories to fetch | 10 |
| `--sort` | `-s` | Sort by: `stars`, `updated`, `best-match` | `stars` |
| `--order` | `-o` | Sort order: `asc`, `desc` | `desc` |
| `--language` | `-l` | Filter by programming language | None |
| `--min-stars` | | Minimum star count | 0 |
| `--download-dir` | `-d` | Download directory | `downloaded_repos` |
| `--method` | `-m` | Download method: `clone`, `zip` | `clone` |
| `--metadata-file` | | CSV filename for metadata | `repository_metadata.csv` |
| `--token` | | GitHub personal access token | From `.env` file |
| `--search-only` | | Only search, don't download | False |

## Smart Folder Organization

The tool automatically creates organized folders for both downloads and metadata:

```
📁 Project Structure:
├── downloaded_repos/                    # Repository downloads
│   ├── machine_learning/
│   ├── react_components_javascript/
│   ├── neural_networks_python_min100stars/
│   └── blockchain_implementation/
└── metadata/                           # CSV metadata files
    ├── machine_learning_repository_metadata.csv
    ├── react_components_javascript_repository_metadata.csv
    ├── neural_networks_python_min100stars_repository_metadata.csv
    └── blockchain_implementation_repository_metadata.csv
```

### Folder Naming Rules:
- **Base name**: Derived from search query (spaces → underscores, special chars removed)
- **Language suffix**: Added when language filter is used (e.g., `_python`, `_javascript`)
- **Star suffix**: Added when minimum stars filter is used (e.g., `_min100stars`)
- **Length limit**: Folder names are limited to 50 characters for compatibility

## Output

The tool creates:

1. **Downloaded repositories**: In topic-organized folders within `downloaded_repos/`
2. **Metadata CSV files**: Stored in the `metadata/` folder with topic-based naming, containing detailed information about each repository:
   - Repository name and full name
   - Description
   - Star and fork counts
   - Programming language
   - URLs (GitHub page and clone URL)
   - Size, creation/update dates
   - Topics information
   - Download timestamp

## Examples

### Research Use Cases

```bash
# Collect transformer architecture implementations
python github_code_fetcher.py -q "transformer architecture" -l python --min-stars 50 -n 20

# Find quantum computing libraries
python github_code_fetcher.py -q "quantum computing" -s stars -n 15

# Get recent graph neural network projects
python github_code_fetcher.py -q "graph neural networks" -s updated -n 10
```

### Learning and Study

```bash
# Find well-documented React projects
python github_code_fetcher.py -q "react tutorial" --min-stars 100 -n 10

# Collect data science notebooks
python github_code_fetcher.py -q "data science jupyter" -l "Jupyter Notebook" -n 25

# Get microservices examples
python github_code_fetcher.py -q "microservices architecture" -l python -n 15
```

## Tips for Better Results

1. **Use specific terms**: Instead of "AI", try "machine learning", "deep learning", or "neural networks"
2. **Combine keywords**: "react typescript components", "python web scraping", etc.
3. **Filter by language**: Use `-l python`, `-l javascript`, etc. for language-specific results
4. **Set minimum stars**: Use `--min-stars` to find well-maintained projects
5. **Try different sorting**: Use `-s updated` to find recently active projects

## Troubleshooting

### Common Issues

1. **Rate limiting**: Create a GitHub token for higher limits
2. **Clone failures**: Try using `-m zip` to download as ZIP files instead
3. **Permission errors**: Check write permissions in the download directory
4. **Network issues**: Ensure stable internet connection for downloads

### Error Messages

- "No repositories found": Try different search terms or reduce filters
- "Git clone failed": Repository might be private or use `-m zip`
- "API rate limit exceeded": Add a GitHub token or wait before retrying

## Dependencies

- `requests`: HTTP requests to GitHub API
- `GitPython`: Git repository cloning
- `pandas`: Data manipulation and CSV export
- `python-dotenv`: Environment variable management
- `tqdm`: Progress bars
- `click`: Command-line interface



## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests for:
- Bug fixes
- Feature enhancements
- Documentation improvements
- Additional search filters
- Performance optimizations
