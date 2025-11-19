import time
import subprocess
import os
import sys

def restart_app():
    """Restart the current Python script."""
    print("Restarting app to apply updates...")
    os.execv(sys.executable, [sys.executable] + sys.argv)

print("Starting app...")
print("Hello Varun, this is the current version of the app.")

# Track last commit hash
last_commit = subprocess.getoutput("git rev-parse HEAD")

while True:
    time.sleep(10)  # check every 10 seconds
    subprocess.run(["git", "pull"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Get current commit hash
    current_commit = subprocess.getoutput("git rev-parse HEAD")
    
    if current_commit != last_commit:
        print("New update detected from GitHub!")
        last_commit = current_commit
        restart_app()
