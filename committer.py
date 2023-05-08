import os
import random
import subprocess
from datetime import datetime, timedelta


def create_commit(date, commit_messages, repo_path):
    commit_date = date.strftime("%Y-%m-%dT%H:%M:%S")

    # Choose a random commit message
    commit_message = random.choice(commit_messages)

    # Create a temporary file to stage for the commit
    temp_file = "temp.txt"
    with open(os.path.join(repo_path, temp_file), "w") as f:
        f.write(commit_message)

    # Stage the temporary file
    subprocess.run(["git", "add", temp_file])

    # Create the commit with the chosen message and date
    subprocess.run(["git", "commit", "--message",
                   commit_message, "--date", commit_date])

    print(f"Commit for {commit_date}: {commit_message}")


def simulate_commits(start_date, end_date, repo_path, commit_chance, min_commits, max_commits, commit_messages):
    current_date = datetime.fromisoformat(start_date)
    end_date_obj = datetime.fromisoformat(end_date)

    while current_date <= end_date_obj:
        if random.random() < commit_chance:
            num_commits = random.randint(min_commits, max_commits)
            for _ in range(num_commits):
                create_commit(current_date, commit_messages, repo_path)
        current_date += timedelta(days=1)

    subprocess.run(["git", "push"])


def main():
    start_date = "2022-01-01"
    end_date = "2022-01-31"
    repo_path = "/path/to/your/local/repo"
    commit_chance = 0.7
    min_commits = 0
    max_commits = 7
    commit_messages = [
        "Update documentation",
        "Refactor code",
        "Add new feature",
        "Fix bug",
        "Improve performance",
        "Update dependencies",
        "Improve code quality",
    ]

    simulate_commits(start_date, end_date, repo_path,
                     commit_chance, min_commits, max_commits, commit_messages)


if __name__ == "__main__":
    main()
