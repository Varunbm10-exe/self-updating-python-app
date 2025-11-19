import time
import subprocess
import os
import sys

def get_current_tag():
    """Return the latest Git tag."""
    tag = subprocess.getoutput("git describe --tags --abbrev=0")
    return tag.strip()

def restart_app():
    """Restart the current Python script."""
    print("Restarting app to apply updates...")
    os.execv(sys.executable, [sys.executable] + sys.argv)

print("Starting app...")
current_tag = get_current_tag()
print(f"Current version: {current_tag}")

while True:
    # Continuous printingggggggggggggggggggggggggggggggg
    print(f"Running version: {current_tag}")
    time.sleep(10)  # print every 10 seconds

    # Pull latest changes and fetch tags
    subprocess.run(["git", "pull"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    subprocess.run(["git", "fetch", "--tags"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Check if tag changed
    new_tag = get_current_tag()
    if new_tag != current_tag:
        print(f"New version detected: {new_tag}")
        current_tag = new_tag
        restart_app()
