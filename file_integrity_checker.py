import hashlib
import os
import json
import pyfiglet
from colorama import Fore, Style, init
from datetime import datetime

# Initialize colorama to reset color settings after each use
init(autoreset=True)

# Supported hashing algorithms options 
HASH_ALGORITHMS = ['md5', 'sha1', 'sha256']

def show_logo():
    """Generate and display the logo using pyfiglet."""
    text_logo = "File Integrity Checker"
    ascii_art = pyfiglet.figlet_format(text_logo)
    print(Fore.CYAN + ascii_art) # Display logo in cyan
    print(Fore.BLUE + "Created by - Premkumar Soni")

def compute_file_hash(filepath, algo='sha256'):
    """Calculate the hash for a given file."""
    if algo not in HASH_ALGORITHMS:
        print(f"{Fore.RED}Error: Unsupported algorithm '{algo}'. Supported algorithms are: {', '.join(HASH_ALGORITHMS)}")
        return None

    hash_function = hashlib.new(algo)
    try:
        with open(filepath, 'rb') as file:
            while chunk := file.read(8192):
                hash_function.update(chunk)
        return hash_function.hexdigest()
    except FileNotFoundError:
        print(f"{Fore.RED}Error: File {filepath} not found.")
        return None

def read_saved_hashes(file='hashes.json'):
    """Load stored hashes from a file."""
    if os.path.exists(file):
        try:
            with open(file, 'r') as hash_file:
                saved_hashes = json.load(hash_file)
                for key in saved_hashes:
                    if isinstance(saved_hashes[key], str):
                        saved_hashes[key] = {
                            'hash': saved_hashes[key],
                            'timestamp': "N/A", 
                            'history': []
                        }
                return saved_hashes
        except (json.JSONDecodeError, ValueError):
            print(f"{Fore.RED}Warning: {file} contains invalid JSON. Initializing as an empty JSON object.")
            return {}
    return {}

def store_hashes(hashes, file='hashes.json'):
    """Save hashes to a file."""
    with open(file, 'w') as hash_file:
        json.dump(hashes, hash_file, indent=4)

def validate_file_integrity(filepath, algo='sha256', hashes_file='hashes.json'):
    """Check the integrity of a file and log modification history."""
    saved_hashes = read_saved_hashes(hashes_file)
    new_hash = compute_file_hash(filepath, algo)

    if new_hash:
        print(f"{Fore.YELLOW}Hash for {filepath} ({algo}): {Fore.CYAN}{new_hash}")
        key = f"{filepath}:{algo}" 

        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        if key in saved_hashes:
            print(f"{Fore.MAGENTA}Stored hash: {saved_hashes[key]['hash']} (Last checked: {saved_hashes[key]['timestamp']})")
            if saved_hashes[key]['hash'] == new_hash:
                print(f"{Fore.GREEN}No changes detected for {filepath} using {algo}. Last checked on {saved_hashes[key]['timestamp']}.")
            else:
                print(f"{Fore.RED}WARNING: {filepath} has been modified using {algo}! (Stored: {saved_hashes[key]['hash']}, Current: {new_hash})")
                saved_hashes[key]['history'].append({
                    'previous_hash': saved_hashes[key]['hash'],
                    'timestamp': timestamp
                })
        else:
            print(f"{Fore.BLUE}New file detected: {filepath}. Storing its hash.")

        saved_hashes[key] = {
            'hash': new_hash,
            'timestamp': timestamp,
            'history': saved_hashes.get(key, {}).get('history', [])
        }

        store_hashes(saved_hashes, hashes_file)

def display_history(filepath, algo='sha256', hashes_file='hashes.json'):
    """Show the modification history of a file."""
    saved_hashes = read_saved_hashes(hashes_file)
    key = f"{filepath}:{algo}" 

    if key in saved_hashes:
        history = saved_hashes[key].get('history', [])
        if history:
            print(f"{Fore.YELLOW}Modification history for {filepath} ({algo}):")
            for record in history:
                print(f"{Fore.CYAN}Previous Hash: {record['previous_hash']} | Timestamp: {record['timestamp']}")
        else:
            print(f"{Fore.GREEN}No modification history available for {filepath} ({algo}).")
    else:
        print(f"{Fore.RED}No records found for {filepath} ({algo}).")

def monitor_files(file_list, algo='sha256', hashes_file='hashes.json'):
    """Monitor multiple files' integrity."""
    if algo not in HASH_ALGORITHMS:
        print(f"{Fore.RED}Error: Unsupported algorithm '{algo}'. Supported algorithms are: {', '.join(HASH_ALGORITHMS)}")
        return

    for filepath in file_list:
        validate_file_integrity(filepath, algo, hashes_file)

if __name__ == "__main__":
    show_logo()

    file_paths_input = input(f"{Fore.YELLOW}Enter the file paths to monitor (separate multiple paths with commas):\n{Fore.GREEN}")
    files_to_monitor = [file.strip() for file in file_paths_input.split(",")]

    print(f"{Fore.YELLOW}Select a hash algorithm:")
    for i, algo in enumerate(HASH_ALGORITHMS, start=1):
        print(f"{Fore.CYAN}{i}. {algo}")
    choice = input(f"{Fore.GREEN}Enter the number corresponding to your choice: ")

    try:
        selected_algorithm = HASH_ALGORITHMS[int(choice) - 1]
        print(f"{Fore.GREEN}Selected algorithm: {selected_algorithm}")

        monitor_files(files_to_monitor, selected_algorithm)

        view_history = input(f"{Fore.YELLOW}Do you want to view the modification history of any file? (yes/no): {Fore.GREEN}").strip().lower()
        if view_history == 'yes':
            file_to_view = input(f"{Fore.YELLOW}Enter the file path for which you want to view history: {Fore.GREEN}").strip()
            display_history(file_to_view, selected_algorithm)
    except (IndexError, ValueError):
        print(f"{Fore.RED}Invalid choice. Please run the program again and select a valid option.")
