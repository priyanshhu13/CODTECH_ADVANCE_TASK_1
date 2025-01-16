# CODETECH_ADVANCE_TASK_1
# File Integrity Checker
# Personal Details
- Name : Premkumar Soni 
- Company : CODTECH IT SOLUTIONS PVT.LTD
- ID : CT08DBS
- Domain : Cyber Security & Ethical Hacking
- Duration: 20th Dec 2024 To 20th Jan 2025
- Mentor : Neela Santhosh Kumar 
# Overview

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
## Screenshot
![image](https://github.com/user-attachments/assets/2cb1203d-ed90-4e8d-a61f-1aff78507d09)

## Example

### Detecting Changes:
```bash
 _____ _ _        ___       _                  _ _
|  ___(_) | ___  |_ _|_ __ | |_ ___  __ _ _ __(_) |_ _   _
| |_  | | |/ _ \  | || '_ \| __/ _ \/ _` | '__| | __| | | |
|  _| | | |  __/  | || | | | ||  __/ (_| | |  | | |_| |_| |
|_|   |_|_|\___| |___|_| |_|\__\___|\__, |_|  |_|\__|\__, |
                                    |___/            |___/
  ____ _               _
 / ___| |__   ___  ___| | _____ _ __
| |   | '_ \ / _ \/ __| |/ / _ \ '__|
| |___| | | |  __/ (__|   <  __/ |
 \____|_| |_|\___|\___|_|\_\___|_|


u:\CODTECH INTERNSHIP\CODTECH ADV TASK\TASK 1\example_file.txt
Select a hash algorithm:
1. md5
2. sha1
3. sha256
Enter the number corresponding to your choice: 1
Selected algorithm: md5
Hash for u:\CODTECH INTERNSHIP\CODTECH ADV TASK\TASK 1\example_file.txt (md5): 62298bbc1b0affa31e5f31f1d8fed82f
Stored hash: b415b32cbf036c7af9bfba6f7fbaa8ef (Last checked: 2025-01-16 15:09:44)
WARNING: u:\CODTECH INTERNSHIP\CODTECH ADV TASK\TASK 1\example_file.txt has been modified using md5! (Stored: b415b32cbf036c7af9bfba6f7fbaa8ef, Current: 62298bbc1b0affa31e5f31f1d8fed82f)
Do you want to view the modification history of any file? (yes/no): yes
Enter the file path for which you want to view history: u:\CODTECH INTERNSHIP\CODTECH ADV TASK\TASK 1\example_file.txt        
Modification history for u:\CODTECH INTERNSHIP\CODTECH ADV TASK\TASK 1\example_file.txt (md5):
Previous Hash: b415b32cbf036c7af9bfba6f7fbaa8ef | Timestamp: 2025-01-16 15:10:18
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

