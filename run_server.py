#!/usr/bin/env python
"""
Direct server runner for Avatar project
Bypasses uvicorn command line issues
"""
import sys
import os

# Add project root to Python path
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    import uvicorn
except ImportError:
    print("ERROR: uvicorn not installed!")
    print("Please run: pip install uvicorn")
    sys.exit(1)

def main():
    print("=" * 45)
    print("     AVATAR SERVER STARTING")
    print("=" * 45)
    print()
    print("🌐 Server URL: http://127.0.0.1:8000")
    print("📖 API Docs:  http://127.0.0.1:8000/docs")
    print("🛑 Stop:      Press Ctrl+C")
    print()
    print("=" * 45)
    print()
    
    try:
        # Run the server
        uvicorn.run(
            "app.main:app",
            host="127.0.0.1",
            port=8000,
            reload=True,
            log_level="info"
        )
    except KeyboardInterrupt:
        print("\n\n✅ Server stopped gracefully")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\nPossible solutions:")
        print("1. Make sure you're in the Avatar-v1 directory")
        print("2. Check that all dependencies are installed")
        print("3. Verify .env file exists with API keys")
        input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()