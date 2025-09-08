"""
Script to check and fix pydantic imports in the project
"""
import os
import re

def fix_pydantic_imports(file_path):
    """Fix pydantic v2 imports to v1 compatible"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Common fixes
    replacements = {
        'from pydantic import BaseSettings': 'from pydantic import BaseSettings',
        'from pydantic_settings import BaseSettings': 'from pydantic import BaseSettings',
        'from pydantic import ConfigDict': '',
        'model_config = ConfigDict': '# model_config removed for v1',
        'from pydantic.v1': 'from pydantic',
    }
    
    original = content
    for old, new in replacements.items():
        content = content.replace(old, new)
    
    # Remove v2 specific code
    content = re.sub(r'model_config\s*=\s*{[^}]+}', '# model_config removed', content)
    content = re.sub(r'ConfigDict\([^)]+\)', '# ConfigDict removed', content)
    
    if content != original:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def check_project():
    """Check all Python files in the project"""
    root = r"D:\My_Projects\Avatar-v1"
    fixed_files = []
    
    for dirpath, dirnames, filenames in os.walk(root):
        # Skip venv directories
        if 'venv' in dirpath or '__pycache__' in dirpath:
            continue
            
        for filename in filenames:
            if filename.endswith('.py'):
                filepath = os.path.join(dirpath, filename)
                try:
                    if fix_pydantic_imports(filepath):
                        fixed_files.append(filepath)
                        print(f"Fixed: {filepath}")
                except Exception as e:
                    print(f"Error processing {filepath}: {e}")
    
    if fixed_files:
        print(f"\nFixed {len(fixed_files)} files")
    else:
        print("\nNo files needed fixing")

if __name__ == "__main__":
    print("Checking project for pydantic compatibility issues...")
    check_project()
    print("\nDone! Now try running the server again.")