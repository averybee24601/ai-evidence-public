import os

# Define the operations to perform
# (action, filepath)
# actions: "delete", "rename"
# for rename, filepath is (old, new)

operations = [
    # Testimony swaps
    ("delete", "data/Testimonies/My Testimony.txt"),
    ("rename", ("data/Testimonies/My Testimony (2).txt", "data/Testimonies/My Testimony.txt")),
    ("delete", "data/Testimonies/Employee Testimony - Juliana (2).txt"),

    # Exact duplicates in Analyzed vs Potential (Delete potential)
    ("delete", "data/potential files to analyze/brewability promotes girls night out.png"),
    ("delete", "data/potential files to analyze/Girls night out.png"),
    ("delete", "data/potential files to analyze/ignores concerns.png"),
    ("delete", "data/potential files to analyze/jose dancing girls night out.mp4"),
    ("delete", "data/potential files to analyze/Jose Special Performance.png"),
    ("delete", "data/potential files to analyze/manipulating people into drag shows with charity fundraisers.png"),
    ("delete", "data/potential files to analyze/pony little moses jones.mp4"),
    ("delete", "data/potential files to analyze/popup queen.png"),
    ("delete", "data/potential files to analyze/promotion of inappropriate holiday parties around adults with disabilities.png"),
    ("delete", "data/potential files to analyze/promotion of lgbtq propoganda.png"),

    # Duplicates within Analyzed (Delete copies)
    ("delete", "data/Analyzed files/Jose Special Performance (2).png"),
    ("delete", "data/Analyzed files/photo_drag_performer_nun_style_group_brewability (2).png"),
    ("delete", "data/Analyzed files/pony little moses jones (2).mp4"),
]

def execute_operations():
    cwd = os.getcwd()
    for action, path_data in operations:
        try:
            if action == "delete":
                # Handle long paths on Windows
                filepath = os.path.join(cwd, path_data)
                if os.name == 'nt' and len(filepath) > 250 and not filepath.startswith('\\\\?\\'):
                    filepath = '\\\\?\\' + filepath
                
                if os.path.exists(filepath):
                    print(f"Deleting: {path_data}")
                    os.remove(filepath)
                else:
                    print(f"File not found (skipped): {path_data}")
                    
            elif action == "rename":
                old_rel, new_rel = path_data
                old_path = os.path.join(cwd, old_rel)
                new_path = os.path.join(cwd, new_rel)
                
                # Handle long paths
                if os.name == 'nt' and (len(old_path) > 250 or len(new_path) > 250):
                    if not old_path.startswith('\\\\?\\'): old_path = '\\\\?\\' + old_path
                    if not new_path.startswith('\\\\?\\'): new_path = '\\\\?\\' + new_path

                if os.path.exists(old_path):
                    print(f"Renaming: {old_rel} -> {new_rel}")
                    if os.path.exists(new_path):
                        print(f"Warning: Target file {new_rel} already exists. Overwriting.")
                        os.remove(new_path)
                    os.rename(old_path, new_path)
                else:
                    print(f"Source file not found (skipped): {old_rel}")

        except Exception as e:
            print(f"Error processing {path_data}: {e}")

if __name__ == "__main__":
    execute_operations()

