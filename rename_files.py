import os

directory = "data/AR"

for filename in os.listdir(directory):
    new_name = None
    if filename.startswith("Analysis of Girls night out") and filename.endswith("(2).txt"):
        new_name = "Analysis_Girls_night_out_combined_2.txt"
    elif filename.startswith("Analysis of Girls night out") and filename.endswith(".txt"):
        new_name = "Analysis_Girls_night_out_combined.txt"
    elif filename.startswith("Analysis of promotion of inappropriate holiday") and filename.endswith("(2).txt"):
        new_name = "Analysis_promotion_inappropriate_holiday_combined_2.txt"
    elif filename.startswith("Analysis of promotion of inappropriate holiday") and filename.endswith(".txt"):
        new_name = "Analysis_promotion_inappropriate_holiday_combined.txt"
    elif filename.startswith("Analysis of Girls night out") and filename.endswith(".txt"):
        # Fallback for other variants if any
        pass 

    if new_name:
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_name)
        print(f"Renaming {filename[:30]}... to {new_name}")
        try:
            os.rename(old_path, new_path)
            print("Success")
        except Exception as e:
            print(f"Error: {e}")

