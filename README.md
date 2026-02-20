# leetcode-setup-cli

Small CLI to initialize a LeetCode workspace quickly with the problem description so you can focus on solving problems and submitting them directly to your GitHub.

**Summary**

- **Purpose:** Fetches a LeetCode problem and scaffolds a directory with a `README.md` and an optional solution file.
- **Language:** Python

**Requirements**

- Python 3.8+
- See `requirements.txt` for dependencies

**Install**

```bash
python3 -m pip install -r requirements.txt
```

**Usage**

```bash
python3 inileet.py <question_id> [options]
```

| Argument / Flag         | Description                                                                                  |
| ----------------------- | -------------------------------------------------------------------------------------------- |
| `question_id`           | LeetCode question number (e.g. `1`, `42`, `200`)                                             |
| `-d`, `--default`       | Skip all prompts — auto-creates the problem directory, `README.md`, and a Java solution file |
| `-l`, `--lang LANGUAGE` | Language for the solution file (default: `java`)                                             |

**Supported languages:** `python`, `java`, `cpp`, `c`, `javascript`, `ruby`, `go`, `csharp`, `swift`, `kotlin`

**Examples**

```bash
# Interactive mode — prompts for each step
python3 inileet.py 1

# Default mode — no prompts, creates directory + README + Java solution
python3 inileet.py 1 -d

# Default mode with a specific language
python3 inileet.py 1 -d -l python

# Interactive mode, but language pre-selected
python3 inileet.py 1 -l cpp
```

**What it creates (default mode)**

```
1-Two-Sum/
├── README.md        ← formatted problem statement
└── 1-Two-Sum.java   ← empty solution file
```

**Files**

- `inileet.py` — main script
- `requirements.txt` — dependencies

---

<p style="text-align:center;">Made with ❤️ by <a href="https://github.com/mar1shell" style="text-decoration:none; font-weight:bold; font-style:italic;">mar1shell</a></p>
