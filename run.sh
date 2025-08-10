#!/bin/bash
# Convenience script to run GitHub Code Fetcher with virtual environment activated

# Activate virtual environment
source code_fetcher/bin/activate

# Run the GitHub Code Fetcher with all passed arguments
python github_code_fetcher.py "$@"
