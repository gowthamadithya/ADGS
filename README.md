# autodoc
The Automated Documentation Generation System is a Python-based tool designed to streamline the process of generating documentation for software projects. It automatically extracts docstrings from Python code files and generates well-structured Markdown documentation, making it easier for developers to maintain up-to-date documentation with minimal manual intervention. This system aims to reduce the time and effort spent on manually writing documentation, ensuring that your code is always documented and easily accessible.

## Features
**Automatic Docstring Extraction:** The system parses Python code files using the Abstract Syntax Tree (AST) module to extract docstrings from functions, classes, and modules.

**Markdown Output:** The extracted documentation is formatted into a user-friendly Markdown file.

**Directory Scanning:** It scans an entire codebase directory and generates comprehensive documentation from all Python files.

## Usage
```python dgs.py /path/to/your/codebase```
