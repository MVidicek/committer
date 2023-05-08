import os
import random
import subprocess
from datetime import datetime, timedelta

# Set your desired date range
start_date = "2022-01-01"
end_date = "2022-01-31"

# Replace this with the path to your local Git repository
repo_path = "/path/to/your/local/repo"

# A temporary file for the script
temp_file = "temp.txt"

# Predefined commit messages
commit_messages = [
    "Update documentation",
    "Refactor code",
    "Fix bug",
    "Add new feature",
    "Improve performance",
    "Add tests",
    "Update dependencies",
    "Improve user experience",
]

def create_commit(date):
    message = random.choice(commit_messages)
    print(f"Commit for {date}: {message}")

    with open(os.path.join(repo_path, temp_file), "w") as f:
        f.write(str(date))

    os.chdir(repo_path)
    subprocess.run(["git", "add", temp_file])
    subprocess.run(["git", "commit", "--date", str(date), "-m", message])

def random_commits(date):
    num_commits = random.randint(0, 7)  # Generate a random number between 0 and 7
    for _ in range(num_commits):
        create_commit(date)

current_date = datetime.fromisoformat(start_date)
end_date_obj = datetime.fromisoformat(end_date)

while current_date <= end_date_obj:
    if random.random() < 0.7:  # 70% chance to create commits on any given day
        random_commits(current_date)

    current_date += timedelta(days=1)

# Push the commits to the remote repository
subprocess.run(["git", "push"])