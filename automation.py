import os

# List of suspicious keywords to scan for
suspicious_keywords = ["password", "secret", "token", "DROP TABLE", "rm -rf"]

def scan_file(file_path):
    """Scans a single file for suspicious keywords."""
    print(f"--- Scanning file: {file_path} ---")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read().lower()
        
        found = False
        for keyword in suspicious_keywords:
            if keyword.lower() in content:
                print(f"[!] ALERT: Keyword '{keyword}' found in {file_path}")
                found = True
        
        if not found:
            print(f"[+] Clean: No suspicious keywords found.")

    except Exception as e:
        print(f"[x] Error reading {file_path}: {e}")

def scan_directory(directory_path):
    """Walks through a directory and scans all .txt and .py files."""
    if not os.path.exists(directory_path):
        print(f"Error: The path '{directory_path}' does not exist.")
        return

    for root, dirs, files in os.walk(directory_path):
        for file in files:
            # Check for specific file extensions
            if file.endswith(".txt") or file.endswith(".py"):
                full_path = os.path.join(root, file)
                scan_file(full_path)

# --- Execution ---
# Using 'r' before the string to handle Windows backslashes correctly
target_folder = r"C:\Users\ASUS\Documents\study\programming\python alzeroes\suspicious_keywords"
scan_directory(target_folder)
