import os
import hashlib
import shutil

# Function to generate file hash (MD5 or SHA256)
def hash_file(file_path, hash_algorithm="md5"):
    hash_algo = hashlib.md5() if hash_algorithm == "md5" else hashlib.sha256()
    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):  # Read file in chunks to avoid memory issues with large files
            hash_algo.update(chunk)
    return hash_algo.hexdigest()

# Function to find duplicate files
def find_duplicates(directory, hash_algorithm="md5"):
    file_hashes = {}
    duplicates = []

    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            file_hash = hash_file(file_path, hash_algorithm)
            
            if file_hash in file_hashes:
                duplicates.append((file_path, file_hashes[file_hash]))
            else:
                file_hashes[file_hash] = file_path

    return duplicates

# Function to handle duplicate files
def handle_duplicates(duplicates, action="alert"):
    for duplicate_file, original_file in duplicates:
        if action == "delete":
            os.remove(duplicate_file)
            print(f"Deleted duplicate: {duplicate_file}")
        else:
            print(f"Duplicate found:\n  Original: {original_file}\n  Duplicate: {duplicate_file}")

# Directory to search for duplicates
# directory = os.path.join(os.path.expanduser("~"), "Fort Kochi")
directory = "/Users/admin/Downloads/Fort Kochi/Documents"

# Find duplicates in the directory using MD5 or SHA256
duplicates = find_duplicates(directory, hash_algorithm="md5")

# Handle duplicates (either alert or delete)
if duplicates:
    handle_duplicates(duplicates, action="alert")  # Change "alert" to "delete" to automatically delete duplicates
else:
    print("No duplicate files found.")