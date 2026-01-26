import os
from pathlib import Path

# Check current working directory
print("Current directory:", os.getcwd())

# Check script's actual location
script_path = Path(__file__).resolve()
print("Script location:", script_path)

# Check if .env exists in current directory
env_file = Path(".env")
print(".env exists in current dir?", env_file.exists())
if env_file.exists():
    print("Full path:", env_file.resolve())
    print("File size:", env_file.stat().st_size, "bytes")
else:
    print("Files in current directory:", list(Path(".").glob("*")))
