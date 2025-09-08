"""
Simple launcher for Avatar project
Works around Windows/PowerShell issues
"""
import subprocess
import sys
import os
import time

def main():
    print("=" * 50)
    print("AVATAR PROJECT LAUNCHER")
    print("=" * 50)
    print()
    
    # Change to project directory
    project_dir = r"D:\My_Projects\Avatar-v1"
    os.chdir(project_dir)
    
    # Find Python executable
    venv_paths = [
        r"venv_new\Scripts\python.exe",
        r"venv\Scripts\python.exe",
        sys.executable
    ]
    
    python_exe = None
    for path in venv_paths:
        if os.path.exists(path):
            python_exe = path
            print(f"Using Python: {path}")
            break
    
    if not python_exe:
        print("ERROR: No Python environment found!")
        input("Press Enter to exit...")
        return
    
    # Check if uvicorn is installed
    try:
        subprocess.run([python_exe, "-m", "uvicorn", "--version"], 
                      capture_output=True, check=True)
    except:
        print("Installing uvicorn...")
        subprocess.run([python_exe, "-m", "pip", "install", "uvicorn"])
    
    print()
    print("Starting server...")
    print("URL: http://127.0.0.1:8000")
    print("Press Ctrl+C to stop")
    print("=" * 50)
    print()
    
    # Start the server
    try:
        subprocess.run([
            python_exe, "-m", "uvicorn", 
            "app.main:app", 
            "--reload", 
            "--host", "127.0.0.1", 
            "--port", "8000"
        ])
    except KeyboardInterrupt:
        print("\n\nServer stopped.")
    except Exception as e:
        print(f"\nError: {e}")
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()