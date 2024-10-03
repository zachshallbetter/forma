#!/usr/bin/env python3

import os
import subprocess
import sys

def run_command(command):
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {command}")
        print(f"Error message: {e}")
        sys.exit(1)

def main():
    venv_path = "/Users/zachshallbetter/Sites/forma/venv"
    
    # Deactivate the current virtual environment (if active)
    run_command("deactivate 2>/dev/null || true")
    
    # Remove the existing virtual environment
    run_command(f"rm -rf {venv_path}")
    
    # Create a new virtual environment with Python 3.10
    run_command(f"python3.10 -m venv {venv_path}")
    
    # Activate the new virtual environment
    activate_script = f"{venv_path}/bin/activate"
    print(f"To activate the new virtual environment, run:")
    print(f"source {activate_script}")

if __name__ == "__main__":
    main()
