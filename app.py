import time
import subprocess
import os
import sys

def get_current_tag():
    """
    Get the latest Git tag from the current commit.
    Uses `git describe --tags --abbrev=0` to find the nearest tag.
    """
    tag = subprocess.getoutput("git describe --tags --abbrev=0")
    print(f"[DEBUG] Current tag from git: {tag}")
    return tag.strip()

def restart_app():
    """
    Restart the current Python script using os.execv.
    This ensures the updated code runs after pulling changes.
    """
    print("Restarting app to apply updates...")
    os.execv(sys.executable, [sys.executable] + sys.argv)

print("Starting app ...")
current_tag = get_current_tag()
print(f"Current version: {current_tag}")

while True:
    # Continuous heartbeat message
    print(f"Running version varunnn: {current_tag}")
    time.sleep(10)  # Check every 10 seconds

    # Pull latest changes from GitHub
    subprocess.run(["git", "pull", "origin", "main"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    subprocess.run(["git", "fetch", "--tags"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Check if tag changed
    new_tag = get_current_tag()
    if new_tag != current_tag:
        print(f"New version detected: {new_tag}")
        current_tag = new_tag
        restart_app()
