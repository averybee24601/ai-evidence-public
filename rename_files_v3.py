import os

cwd = os.getcwd()
directory = os.path.join(cwd, "data", "AR")
long_path_directory = "\\\\?\\" + directory

for filename in os.listdir(directory):
    new_name = None
    if filename.startswith("Analysis of Girls night out") and filename.endswith("Jose Special Performance.png.txt"):
         new_name = "Analysis_Girls_night_out_combined_full.txt"

    if new_name:
        old_path = os.path.join(long_path_directory, filename)
        new_path = os.path.join(long_path_directory, new_name)
        print(f"Renaming {filename[:30]}... to {new_name}")
        try:
            os.rename(old_path, new_path)
            print("Success")
        except Exception as e:
            print(f"Error: {e}")

