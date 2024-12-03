import ast
import os

def extract_docstrings_from_file(file_path):
    """Extract docstrings from a Python file."""
    with open(file_path, "r", encoding="utf-8") as file:  # Added encoding='utf-8'
        tree = ast.parse(file.read())
    
    docstrings = []
    
    # Walk through all nodes and look for function and class definitions
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            doc = ast.get_docstring(node)
            if doc:
                docstrings.append({
                    "name": node.name,
                    "type": "Function" if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) else "Class",
                    "docstring": doc
                })
    return docstrings

def generate_markdown(docstrings):
    """Generate a Markdown file from the extracted docstrings."""
    markdown = "# Documentation\n\n"
    
    for doc in docstrings:
        markdown += f"## {doc['type']}: {doc['name']}\n\n"
        markdown += f"```text\n{doc['docstring']}\n```\n\n"
    
    return markdown

def generate_documentation_for_directory(directory_path):
    """Scan a directory and generate documentation for all Python files."""
    if not os.path.isdir(directory_path):
        print(f"The path '{directory_path}' is not a valid directory.")
        return
    
    all_docstrings = []
    
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                print(f"Processing file: {file_path}")  # Optionally add a print to see progress
                docstrings = extract_docstrings_from_file(file_path)
                all_docstrings.extend(docstrings)
    
    if all_docstrings:
        markdown_content = generate_markdown(all_docstrings)
        
        # Write the Markdown content to a file
        with open("documentation.md", "w", encoding="utf-8") as doc_file:
            doc_file.write(markdown_content)
        print("Documentation generated as 'documentation.md'.")
    else:
        print("No docstrings found in the specified directory.")

#Example usage
current_dir = os.path.dirname(os.path.abspath(__file__))  # Get the current directory
code_path = os.path.join(current_dir, "samplecode")
generate_documentation_for_directory(code_path)
