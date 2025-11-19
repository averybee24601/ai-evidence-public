import os

# Use absolute path with \\?\ prefix to bypass MAX_PATH limit on Windows
cwd = os.getcwd()
directory = os.path.join(cwd, "data", "AR")
long_path_directory = "\\\\?\\" + directory

print(f"Processing directory: {long_path_directory}")

for filename in os.listdir(directory): # listdir works on the normal path usually, or I can use the long path
    new_name = None
    if filename.startswith("Analysis of Girls night out") and filename.endswith("(2).txt"):
        new_name = "Analysis_Girls_night_out_combined_2.txt"
    elif filename.startswith("Analysis of Girls night out") and filename.endswith(".txt") and len(filename) > 100:
        new_name = "Analysis_Girls_night_out_combined.txt"
    elif filename.startswith("Analysis of promotion of inappropriate holiday") and filename.endswith("(2).txt"):
        new_name = "Analysis_promotion_inappropriate_holiday_combined_2.txt"
    elif filename.startswith("Analysis of promotion of inappropriate holiday") and filename.endswith(".txt"):
        new_name = "Analysis_promotion_inappropriate_holiday_combined.txt"
    
    if new_name:
        old_path = os.path.join(long_path_directory, filename)
        new_path = os.path.join(long_path_directory, new_name)
        print(f"Renaming {filename[:30]}... to {new_name}")
        try:
            os.rename(old_path, new_path)
            print("Success")
        except Exception as e:
            print(f"Error: {e}")

