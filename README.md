# Suspicious Keyword Scanner 🛡️

![Project Demo](Screenshot%20(1639).png)

## Description
This Python automation tool scans files for sensitive keywords like passwords, tokens, and dangerous commands to help ensure code security.
## 🚀 Features
* **Case-Insensitive Search**: Matches keywords regardless of capitalization.
* **Directory Traversal**: Automatically walks through folders to find `.py` and `.txt` files.
* **Security Alerts**: Specifically looks for high-risk strings like `password`, `DROP TABLE`, and `rm -rf`.
* **Error Handling**: Uses try-except blocks to manage file reading errors gracefully.

## 🛠️ How it Works
The script uses the `os.walk` function to navigate through the specified directory path. It opens each supported file with `utf-8` encoding and compares its content against a pre-defined list of suspicious keywords.

## 💻 Setup
1. Clone this repository.
2. Update the `target_folder` path in `automation.py` to your desired directory.
3. Run the script using Python:
   ```bash
   python automation.py
