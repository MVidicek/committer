# Committer

`Committer` is a customizable Python script that generates a more natural-looking commit history on GitHub by simulating variable commit activity, random commit messages, and commit distribution over a specified date range. 

This script is ideal for testing or personal use, helping users understand and visualize different commit patterns.

**Note:** Artificially inflating your GitHub contribution history can be seen as dishonest or unethical. Use this script responsibly and only for legitimate reasons, such as testing or personal use.

## Requirements

- Python 3.6 or higher
- Git

## Usage

1. Clone or download this repository to your local machine.
2. Modify the `start_date`, `end_date`, and `repo_path` variables in the `committer.py` script to match your desired date range and the path to your local Git repository.
3. Customize the `commit_messages` list in the script if you want to use different commit messages.
4. Open a terminal and navigate to the directory containing the `committer.py` script.
5. Run the script using the following command: `python3 committer.py`.
6. The script will create commits with random messages and varying frequency within the specified date range and push them to the remote repository.

## Customization

You can easily customize the script by modifying the following variables:

- `start_date`: The start date of the commit history (in the format "YYYY-MM-DD").
- `end_date`: The end date of the commit history (in the format "YYYY-MM-DD").
- `repo_path`: The path to your local Git repository.
- `temp_file`: The name of the temporary file used for generating commits. You can change this to a different file name if desired.
- `commit_messages`: A list of predefined commit messages. You can add, remove, or modify these messages to suit your needs.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
