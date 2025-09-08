#!/usr/bin/env python
"""
Test script to check if all imports work correctly
"""
import sys
print(f"Python version: {sys.version}")
print("-" * 50)

def test_import(module_name):
    try:
        module = __import__(module_name)
        version = getattr(module, '__version__', 'unknown')
        print(f"✅ {module_name:<20} version: {version}")
        return True
    except ImportError as e:
        print(f"❌ {module_name:<20} ERROR: {e}")
        return False

print("Testing imports...")
print("-" * 50)

modules = [
    'fastapi',
    'uvicorn', 
    'pydantic',
    'pydantic_core',
    'openai',
    'websockets',
    'aiohttp',
    'pydub',
    'dotenv',
    'requests'
]

failed = []
for module in modules:
    if not test_import(module):
        failed.append(module)

print("-" * 50)

if failed:
    print(f"\n❌ Failed imports: {', '.join(failed)}")
    print("\nRun WINDOWS_SETUP.bat to fix missing dependencies")
else:
    print("\n✅ All imports successful!")
    print("\nTesting app import...")
    try:
        import app.main
        print("✅ app.main imported successfully!")
        print("\nYour project is ready to run!")
        print("Run: python -m uvicorn app.main:app --reload")
    except Exception as e:
        print(f"❌ Error importing app.main: {e}")
        
input("\nPress Enter to exit...")