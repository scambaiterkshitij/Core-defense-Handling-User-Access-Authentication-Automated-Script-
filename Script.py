import os
import subprocess
from datetime import datetime

# Repo path ()
REPO_PATH = "/path/to/your/dummy-repo"

def git_commit():
    os.chdir(REPO_PATH)

    # write timestamp to file
    with open("data.txt", "a") as f:
        f.write(f"Update at {datetime.now()}\n")

    # git add + commit
    subprocess.run(["git", "add", "data.txt"])
    subprocess.run(["git", "commit", "-m", f"auto update {datetime.now()}"])
    subprocess.run(["git", "push", "origin", "main"])

if __name__ == "__main__":
    git_commit()
