#!/usr/bin/env python3
"""
Simple tests for GitHub Code Fetcher

Author: Sreeram (sreeram.lagisetty@gmail.com)
GitHub: https://github.com/Sreeram5678
Repository: https://github.com/Sreeram5678/GITHUB-Code-Fetcher.git
"""

import unittest
from unittest.mock import patch, MagicMock
import tempfile
import os
from pathlib import Path

# Import the main class
from github_code_fetcher import GitHubCodeFetcher, sanitize_folder_name


class TestSanitizeFolderName(unittest.TestCase):
    """Test the sanitize_folder_name function."""
    
    def test_basic_query(self):
        """Test basic query sanitization."""
        result = sanitize_folder_name("machine learning")
        self.assertEqual(result, "machine_learning")
    
    def test_with_language(self):
        """Test query with language filter."""
        result = sanitize_folder_name("neural networks", language="python")
        self.assertEqual(result, "neural_networks_python")
    
    def test_with_min_stars(self):
        """Test query with minimum stars filter."""
        result = sanitize_folder_name("react components", min_stars=100)
        self.assertEqual(result, "react_components_min100stars")
    
    def test_with_special_characters(self):
        """Test query with special characters."""
        result = sanitize_folder_name("c++ algorithms")
        self.assertEqual(result, "c_algorithms")
    
    def test_length_limit(self):
        """Test that folder name is limited to 50 characters."""
        long_query = "a" * 60
        result = sanitize_folder_name(long_query)
        self.assertLessEqual(len(result), 50)


class TestGitHubCodeFetcher(unittest.TestCase):
    """Test the GitHubCodeFetcher class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.fetcher = GitHubCodeFetcher()
    
    def test_init_without_token(self):
        """Test initialization without token."""
        fetcher = GitHubCodeFetcher()
        self.assertIsNone(fetcher.token)
        self.assertEqual(fetcher.base_url, "https://api.github.com")
    
    def test_init_with_token(self):
        """Test initialization with token."""
        token = "test_token_123"
        fetcher = GitHubCodeFetcher(token=token)
        self.assertEqual(fetcher.token, token)
    
    @patch('os.getenv')
    def test_init_with_env_token(self, mock_getenv):
        """Test initialization with token from environment."""
        mock_getenv.return_value = "env_token_456"
        fetcher = GitHubCodeFetcher()
        self.assertEqual(fetcher.token, "env_token_456")
    
    def test_sanitize_folder_name_integration(self):
        """Test that sanitize_folder_name works with the fetcher."""
        # This is a simple integration test
        query = "test query"
        folder_name = sanitize_folder_name(query)
        self.assertIsInstance(folder_name, str)
        self.assertGreater(len(folder_name), 0)


if __name__ == '__main__':
    unittest.main()
