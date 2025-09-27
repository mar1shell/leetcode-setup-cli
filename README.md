# LeetCode Setup CLI

A simple Python utility script to fetch a LeetCode problem description by its ID, format it into a clean Markdown file (`README.md`), and set up a corresponding solution file in a new, dedicated directory.

This script helps developers like me to streamline the process of starting a new LeetCode challenge by automatically creating the necessary files and folder structure.

---

## 🚀 Features

- **Problem Fetching:** Retrieves problem details (ID, Title, Content) from the LeetCode API using a question ID.
- **Markdown Formatting:** Converts the problem's HTML content into clean, readable Markdown (`README.md`).
- **Directory Creation:** Creates a new, structured directory for each problem (e.g., `1-Two-Sum`).
- **Solution File Setup:** Automatically creates an empty solution file inside the problem directory, supporting multiple languages.

---

## 🛠️ Prerequisites

- **Python 3.x**
- The required Python libraries are listed in **`requirements.txt`**.

---

## ⚙️ Installation

1.  **clone the repository** or download the script files to your local machine.

    ```bash
    git clone github.com/mar1shell/leetcode-setup-cli.git
    cd leetcode-setup-cli
    ```

2.  **Install the required libraries** using `pip` and the `requirements.txt` file:

```bash
    pip install -r requirements.txt
```

---

## 🖥️ Usage

The script is executed from the command line, requiring the LeetCode **Question ID** as the first argument and an **optional language** as the second argument.

### 💻 Running on Linux/macOS (Bash)

Use the `python3` command (or `python` if it points to Python 3) followed by the script name.

```bash
python3 inileet.py <questionId> [language]
```

### 🪟 Running on Windows (Command Prompt/PowerShell)

Use the `python` command followed by the script name.

```bash
python inileet.py <questionId> [language]
```

---

<div align="center">
    <p>Made with ❤️ by <strong>mar1shell</strong></p>
    <p>⭐ Star this repo if you found it helpful!</p>
</div>
