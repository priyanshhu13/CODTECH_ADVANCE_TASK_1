# CODETECH_ADVANCE_TASK_1
# Personal Details
- Name : Premkumar Soni 
- Company : CODTECH IT SOLUTIONS PVT.LTD
- ID : CT08DBS
- Domain : Cyber Security & Ethical Hacking
- Duration: 20th Dec 2024 To 20th Jan 2025
- Mentor : Neela Santhosh Kumar 
# File Integrity Checker

The **File Integrity Checker** is a Python tool designed to monitor and verify the integrity of files using hash functions. It allows users to detect file modifications, maintain a history of changes, and ensure data consistency.

---

## Features
- **Multiple Hash Algorithms**: Supports MD5, SHA1, and SHA256.
- **Modification Detection**: Compares stored and current file hashes to identify changes.
- **History Tracking**: Maintains a detailed history of file modifications, including timestamps and previous hash values.
- **Interactive CLI**: User-friendly command-line interface with ASCII art logo.
- **JSON Storage**: Saves file hashes and history in a JSON file for persistent monitoring.

---

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/hipremsoni/CODETECH_ADVANCE_TASK_1.git
    ```
    ```bash
    cd CODETECH_ADVANCE_TASK_1
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the tool : 
    ```bash
    Python3 file_integrity_checker.py
    ```

---

## Usage

1. **Run the program:**
    ```bash
    python3 file_integrity_checker.py
    ```

2. **Enter file paths:**
    Provide one or multiple file paths to monitor, separated by commas.
    
    ```path
    // Example For Windows Path 
    C:\\Example\\file.txt
    ```
    ```path
    //Exaple For Linux Path 
    /home/kali/file.txt

3. **Select a hash algorithm:**
    Choose one of the supported algorithms (MD5, SHA1, SHA256).

4. **Monitor for changes:**
    The tool checks file integrity, stores hashes, and updates the history in `hashes.json`.

5. **View history:**
    Optionally, display the modification history for any file.

---

## Example

### Detecting Changes:
```bash
Enter the file paths to monitor (separate multiple paths with commas):
> example.txt, test_file.txt

Select a hash algorithm:
1. md5
2. sha1
3. sha256
Enter the number corresponding to your choice: 3

Hash for example.txt (sha256): abc123...
No changes detected for example.txt.

Hash for test_file.txt (sha256): def456...
WARNING: test_file.txt has been modified!

Do you want to view the modification history of any file? (yes/no): yes
Enter the file path for which you want to view history: test_file.txt
Modification history for test_file.txt (sha256):
Previous Hash: oldhashvalue | Timestamp: 2024-01-01 12:00:00
```

---

## File Structure
- **`file_integrity_checker.py`**: Main Python script.
- **`hashes.json`**: JSON file storing hashes and modification history.
- **`requirements.txt`**: Dependencies for the project.

---

## Dependencies
- `hashlib`
- `os`
- `json`
- `pyfiglet`
- `colorama`
- `datetime`

---

## Acknowledgements
- **[pyfiglet](https://pypi.org/project/pyfiglet/)** for ASCII art generation.
- **[colorama](https://pypi.org/project/colorama/)** for terminal text formatting.

---

## Author
- **Premkumar Soni**
- [GitHub Profile](https://github.com/yourusername)

