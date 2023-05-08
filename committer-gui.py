import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QSpinBox, QDoubleSpinBox, QPlainTextEdit, QFormLayout, QWidget
from committer import simulate_commits


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        form_layout = QFormLayout()

        self.start_date_input = QLineEdit()
        form_layout.addRow(QLabel("Start date (YYYY-MM-DD):"),
                           self.start_date_input)

        self.end_date_input = QLineEdit()
        form_layout.addRow(QLabel("End date (YYYY-MM-DD):"),
                           self.end_date_input)

        self.repo_path_input = QLineEdit()
        form_layout.addRow(QLabel("Repository path:"), self.repo_path_input)

        self.commit_chance_input = QDoubleSpinBox()
        self.commit_chance_input.setRange(0, 1)
        self.commit_chance_input.setSingleStep(0.1)
        self.commit_chance_input.setValue(0.7)
        form_layout.addRow(QLabel("Commit chance (0-1):"),
                           self.commit_chance_input)

        self.min_commits_input = QSpinBox()
        self.min_commits_input.setRange(0, 100)
        form_layout.addRow(QLabel("Minimum commits per day:"),
                           self.min_commits_input)

        self.max_commits_input = QSpinBox()
        self.max_commits_input.setRange(0, 100)
        self.max_commits_input.setValue(7)
        form_layout.addRow(QLabel("Maximum commits per day:"),
                           self.max_commits_input)

        self.commit_messages_input = QPlainTextEdit()
        form_layout.addRow(
            QLabel("Commit messages (one per line):"), self.commit_messages_input)

        layout.addLayout(form_layout)

        self.generate_button = QPushButton("Generate Commits")
        self.generate_button.clicked.connect(self.generate_commits)
        layout.addWidget(self.generate_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def generate_commits(self):
        start_date = self.start_date_input.text()
        end_date = self.end_date_input.text()
        repo_path = self.repo_path_input.text()
        commit_chance = self.commit_chance_input.value()
        min_commits = self.min_commits_input.value()
        max_commits = self.max_commits_input.value()
        commit_messages = self.commit_messages_input.toPlainText().splitlines()

        simulate_commits(start_date, end_date, repo_path,
                         commit_chance, min_commits, max_commits, commit_messages)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
