import os
import hashlib

def get_file_hash(filepath):
    """Calculates the MD5 hash of a file."""
    hasher = hashlib.md5()
    try:
        with open(filepath, 'rb') as f:
            buf = f.read(65536)
            while len(buf) > 0:
                hasher.update(buf)
                buf = f.read(65536)
        return hasher.hexdigest()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return None

def find_duplicates(start_dir):
    """Finds duplicate files in a directory recursively."""
    hashes = {}
    duplicates = []

    # Use os.walk to traverse the directory
    # Use \\?\ for long paths on Windows
    abs_start_dir = os.path.abspath(start_dir)
    if os.name == 'nt' and not abs_start_dir.startswith('\\\\?\\'):
        abs_start_dir = '\\\\?\\' + abs_start_dir

    for dirpath, _, filenames in os.walk(abs_start_dir):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            file_hash = get_file_hash(filepath)
            
            if file_hash:
                if file_hash in hashes:
                    hashes[file_hash].append(filepath)
                else:
                    hashes[file_hash] = [filepath]

    # Filter for hashes with multiple files
    for file_hash, file_list in hashes.items():
        if len(file_list) > 1:
            duplicates.append(file_list)
            
    return duplicates

if __name__ == "__main__":
    start_directory = "data"
    dupes = find_duplicates(start_directory)
    
    print(f"Found {len(dupes)} sets of duplicates.")
    for i, duplicate_set in enumerate(dupes):
        print(f"\nSet {i+1}:")
        for file in duplicate_set:
            # Print relative path for readability if possible, else full path
            try:
                print(os.path.relpath(file, os.getcwd()))
            except:
                print(file)

