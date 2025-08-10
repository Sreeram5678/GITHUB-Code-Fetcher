# GitHub Code Fetcher - Command Reference

This file contains organized commands and examples for using the GitHub Code Fetcher tool.

## 📁 **NEW: Automatic Topic-Based Folder Organization**

The tool now automatically creates organized folders for both downloads and metadata:

### 📂 **Downloads Folder Structure:**
- **Query**: "machine learning" → `downloaded_repos/machine_learning/`
- **With language**: "react components" + python → `downloaded_repos/react_components_python/`
- **With stars**: "neural networks" + min 100 stars → `downloaded_repos/neural_networks_min100stars/`
- **Combined**: "deep learning" + python + 50 stars → `downloaded_repos/deep_learning_python_min50stars/`

### 📊 **Metadata CSV Organization:**
- All CSV files are automatically stored in the `metadata/` folder
- **Query**: "machine learning" → `metadata/machine_learning_repository_metadata.csv`
- **With filters**: "react components" + python → `metadata/react_components_python_repository_metadata.csv`

This keeps both your downloads AND metadata perfectly organized by topic!

## 🚀 Quick Start Commands

### Basic Setup
```bash
# Activate virtual environment
source code_fetcher/bin/activate

# Using convenience script (automatically activates environment)
./run.sh --help
```

### Simple Searches
```bash
# Basic search (top 10 repositories by stars)
./run.sh -q "machine learning" -n 10

# Search only (no download)
./run.sh -q "machine learning" -n 10 --search-only

# Get help
./run.sh --help
```

## 📚 Learning & Research Commands

### AI/Machine Learning
```bash
# Transformer architecture implementations
./run.sh -q "transformer architecture" -l python --min-stars 50 -n 20

# Neural networks (Python only)
./run.sh -q "neural networks" -l python -n 15

# Deep learning tutorials
./run.sh -q "deep learning tutorial" --min-stars 100 -n 10

# Computer vision projects
./run.sh -q "computer vision opencv" -l python -n 12

# Natural language processing
./run.sh -q "NLP natural language processing" -l python --min-stars 200 -n 15

# Reinforcement learning
./run.sh -q "reinforcement learning" -l python -n 10

# Graph neural networks
./run.sh -q "graph neural networks" -l python --min-stars 30 -n 8
```

### Data Science & Analytics
```bash
# Data science notebooks
./run.sh -q "data science jupyter" -l "Jupyter Notebook" -n 25

# Data analysis projects
./run.sh -q "data analysis pandas" -l python -n 15

# Statistical analysis
./run.sh -q "statistical analysis" -l python --min-stars 50 -n 10

# Data visualization
./run.sh -q "data visualization matplotlib seaborn" -l python -n 12
```

### Web Development
```bash
# React components (high quality)
./run.sh -q "react components" -l javascript --min-stars 100 -n 15

# React TypeScript projects
./run.sh -q "react typescript" -l typescript -n 12

# Vue.js applications
./run.sh -q "vue.js applications" -l javascript -n 10

# Node.js APIs
./run.sh -q "nodejs api express" -l javascript -n 15

# Full-stack applications
./run.sh -q "full stack application" -l javascript --min-stars 50 -n 10
```

### Mobile Development
```bash
# React Native apps
./run.sh -q "react native" -l javascript -n 12

# Flutter applications
./run.sh -q "flutter applications" -l dart -n 10

# iOS Swift projects
./run.sh -q "ios swift" -l swift -n 10

# Android Kotlin projects
./run.sh -q "android kotlin" -l kotlin -n 10
```

## 🔬 Advanced Technology Commands

### Blockchain & Cryptocurrency
```bash
# Blockchain implementations
./run.sh -q "blockchain implementation" -l python --min-stars 100 -n 10

# Smart contracts
./run.sh -q "smart contracts solidity" -l solidity -n 12

# DeFi projects
./run.sh -q "defi decentralized finance" --min-stars 50 -n 8

# Cryptocurrency trading bots
./run.sh -q "cryptocurrency trading bot" -l python -n 10
```

### DevOps & Cloud
```bash
# Kubernetes examples
./run.sh -q "kubernetes examples" --min-stars 100 -n 15

# Docker implementations
./run.sh -q "docker containerization" --min-stars 50 -n 12

# CI/CD pipelines
./run.sh -q "ci cd pipeline" -n 10

# Infrastructure as code
./run.sh -q "terraform infrastructure" -n 8

# Microservices architecture
./run.sh -q "microservices architecture" -l python --min-stars 100 -n 15
```

### Quantum Computing
```bash
# Quantum computing libraries
./run.sh -q "quantum computing" -l python --min-stars 50 -n 10

# Quantum algorithms
./run.sh -q "quantum algorithms qiskit" -l python -n 8

# Quantum machine learning
./run.sh -q "quantum machine learning" -l python -n 6
```

### Cybersecurity
```bash
# Penetration testing tools
./run.sh -q "penetration testing tools" -l python --min-stars 100 -n 12

# Network security
./run.sh -q "network security scanner" -l python -n 10

# Cryptography implementations
./run.sh -q "cryptography implementation" -l python --min-stars 50 -n 8
```

## 🎯 Sorting & Filtering Commands

### By Popularity (Stars)
```bash
# Most starred repositories
./run.sh -q "python web framework" -s stars -o desc -n 10

# High-quality projects only (500+ stars)
./run.sh -q "react hooks" --min-stars 500 -n 8
```

### By Recent Activity
```bash
# Most recently updated
./run.sh -q "javascript framework" -s updated -o desc -n 10

# Recent Python projects
./run.sh -q "python automation" -s updated -l python -n 12
```

### By Relevance
```bash
# Best match for specific query
./run.sh -q "natural language processing transformers" -s best-match -n 15
```

### Language-Specific Searches
```bash
# Python projects only
./run.sh -q "web scraping" -l python -n 10

# JavaScript/TypeScript projects
./run.sh -q "frontend framework" -l javascript -n 8
./run.sh -q "type safety" -l typescript -n 8

# Go projects
./run.sh -q "concurrent programming" -l go -n 10

# Rust projects
./run.sh -q "systems programming" -l rust -n 8

# Java projects
./run.sh -q "spring boot" -l java -n 10
```

## 📁 Download & Storage Commands

### Different Download Methods
```bash
# Clone repositories (default)
./run.sh -q "django tutorial" -l python -n 5

# Download as ZIP files (faster)
./run.sh -q "react tutorial" -l javascript -m zip -n 5

# Custom download directory
./run.sh -q "machine learning" -d ./ai_projects -n 10

# Custom metadata filename
./run.sh -q "web development" --metadata-file web_repos.csv -n 15
```

### Organized Downloads (Automatic Topic-Based Folders)
```bash
# Downloads to: downloaded_repos/frontend_components/
./run.sh -q "frontend components" -n 20

# Downloads to: downloaded_repos/api_backend/
./run.sh -q "api backend" -n 15

# Downloads to: downloaded_repos/artificial_intelligence/
./run.sh -q "artificial intelligence" -n 25

# Downloads to: downloaded_repos/data_science/
./run.sh -q "data science" -n 20

# With language filter: downloaded_repos/machine_learning_python/
./run.sh -q "machine learning" -l python -n 15

# With star filter: downloaded_repos/react_components_min100stars/
./run.sh -q "react components" --min-stars 100 -n 10

# Custom base directory: my_repos/neural_networks_python/
./run.sh -q "neural networks" -l python -d ./my_repos -n 15
```

## 🔍 Specialized Search Commands

### Educational Content
```bash
# Programming tutorials
./run.sh -q "programming tutorial beginner" --min-stars 200 -n 15

# Algorithm implementations
./run.sh -q "algorithm implementation" -l python --min-stars 100 -n 20

# Design patterns
./run.sh -q "design patterns examples" --min-stars 50 -n 10

# Coding interview preparation
./run.sh -q "coding interview leetcode" -l python -n 15
```

### Open Source Projects
```bash
# Popular open source tools
./run.sh -q "open source tool" --min-stars 1000 -n 20

# Developer tools
./run.sh -q "developer productivity tools" --min-stars 200 -n 15

# Command line utilities
./run.sh -q "command line utility" -l python --min-stars 100 -n 12
```

### Industry-Specific
```bash
# Fintech applications
./run.sh -q "fintech banking application" --min-stars 50 -n 10

# Healthcare software
./run.sh -q "healthcare medical software" -l python -n 8

# E-commerce platforms
./run.sh -q "ecommerce platform" --min-stars 100 -n 12

# Gaming engines/tools
./run.sh -q "game engine development" -l "C++" -n 10
```

## 🛠️ Utility Commands

### Project Management
```bash
# Check virtual environment status
source code_fetcher/bin/activate && which python

# View all downloaded topic folders
ls -la downloaded_repos/

# View all metadata files
ls -la metadata/

# Check specific metadata file
head -5 metadata/machine_learning_repository_metadata.csv

# Count downloaded topic folders
ls downloaded_repos/ | wc -l

# Count repositories in a specific topic
ls downloaded_repos/machine_learning/ | wc -l

# View folder structure
tree downloaded_repos/ -L 2
tree metadata/
```

### Maintenance
```bash
# Update dependencies
source code_fetcher/bin/activate && pip install --upgrade -r requirements.txt

# Clean up all downloads (be careful!)
rm -rf downloaded_repos/

# Clean up all metadata files (be careful!)
rm -rf metadata/

# Remove specific topic downloads
rm -rf downloaded_repos/machine_learning/

# Remove specific metadata file
rm metadata/machine_learning_repository_metadata.csv

# Clean up just empty folders
find downloaded_repos/ -type d -empty -delete
```

### Troubleshooting
```bash
# Test connection without downloading
./run.sh -q "test" -n 1 --search-only

# Use ZIP method if git clone fails
./run.sh -q "your_query" -m zip -n 5

# Increase verbosity (if script had verbose mode)
./run.sh -q "your_query" -n 5 --search-only
```

## 📊 Batch Operations

### Multiple Related Searches (Auto-Organized)
```bash
# Search multiple AI topics - automatically organized
./run.sh -q "computer vision" -l python -n 10
# → downloaded_repos/computer_vision_python/

./run.sh -q "natural language processing" -l python -n 10
# → downloaded_repos/natural_language_processing_python/

./run.sh -q "reinforcement learning" -l python -n 10
# → downloaded_repos/reinforcement_learning_python/

# Search different web frameworks - automatically organized
./run.sh -q "react framework" -l javascript -n 8
# → downloaded_repos/react_framework_javascript/

./run.sh -q "vue framework" -l javascript -n 8
# → downloaded_repos/vue_framework_javascript/

./run.sh -q "angular framework" -l typescript -n 8
# → downloaded_repos/angular_framework_typescript/
```

### Language Comparison Studies (Auto-Organized)
```bash
# Same concept in different languages - automatically organized by language
./run.sh -q "web framework" -l python -n 10
# → downloaded_repos/web_framework_python/

./run.sh -q "web framework" -l javascript -n 10
# → downloaded_repos/web_framework_javascript/

./run.sh -q "web framework" -l go -n 10
# → downloaded_repos/web_framework_go/

./run.sh -q "web framework" -l rust -n 10
# → downloaded_repos/web_framework_rust/

# Machine learning in different languages
./run.sh -q "machine learning" -l python -n 15
./run.sh -q "machine learning" -l r -n 10
./run.sh -q "machine learning" -l julia -n 8
```

## 🎓 Study Plans

### Beginner Programming Path
```bash
# 1. Programming fundamentals
./run.sh -q "programming fundamentals tutorial" --min-stars 200 -n 10

# 2. Data structures and algorithms
./run.sh -q "data structures algorithms python" --min-stars 500 -n 15

# 3. Web development basics
./run.sh -q "web development beginner" --min-stars 100 -n 12

# 4. Project examples
./run.sh -q "beginner programming projects" --min-stars 50 -n 20
```

### Advanced AI/ML Path
```bash
# 1. Mathematical foundations
./run.sh -q "machine learning mathematics" -l python --min-stars 100 -n 10

# 2. Classical ML algorithms
./run.sh -q "scikit-learn machine learning" -l python --min-stars 200 -n 15

# 3. Deep learning frameworks
./run.sh -q "tensorflow keras tutorial" -l python --min-stars 300 -n 12

# 4. Advanced topics
./run.sh -q "transformer attention mechanism" -l python --min-stars 100 -n 10

# 5. Practical applications
./run.sh -q "machine learning production deployment" -l python --min-stars 50 -n 15
```

---

## 💡 Pro Tips

1. **Use specific terms**: "transformer architecture" vs "AI"
2. **Combine keywords**: "react typescript hooks" 
3. **Filter by stars**: Use `--min-stars` for quality projects
4. **Try different sorting**: `-s updated` for recent projects
5. **Test searches first**: Use `--search-only` to preview results
6. **Organize downloads**: Use `-d` to separate projects by topic
7. **Check metadata**: Review CSV files before downloading large batches

## 🔗 Quick Reference

| Flag | Description | Example |
|------|-------------|---------|
| `-q` | Search query | `-q "machine learning"` |
| `-n` | Max results | `-n 20` |
| `-l` | Language filter | `-l python` |
| `-s` | Sort method | `-s stars` or `-s updated` |
| `-d` | Download directory | `-d ./my_repos` |
| `-m` | Download method | `-m zip` or `-m clone` |
| `--min-stars` | Minimum stars | `--min-stars 100` |
| `--search-only` | No download | `--search-only` |
