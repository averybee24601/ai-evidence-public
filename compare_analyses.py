import os

pairs = [
    ("data/AR/Analysis of screenshot_denver_pride_checklist_full.png.txt", "data/AR/Analysis of screenshot_denver_pride_checklist_full.png (2).txt"),
    ("data/AR/Analysis of text.png.txt", "data/AR/Analysis of text.png (2).txt"),
    ("data/AR/Analysis of 4de7b953-310e-43e7-9e05-a966c4f05935 (1) (3).mp4.txt", "data/AR/Analysis of 4de7b953-310e-43e7-9e05-a966c4f05935 (1) (3).mp4 (2).txt"),
    ("data/AR/Analysis_Girls_night_out_combined.txt", "data/AR/Analysis_Girls_night_out_combined_2.txt"),
    ("data/AR/Analysis_menu_promotion_combined.txt", "data/AR/Analysis_menu_promotion_combined_2.txt"),
    ("data/AR/Analysis_menu_promotion_combined.txt", "data/AR/Analysis_menu_promotion_combined_3.txt"),
    ("data/AR/Analysis_promotion_inappropriate_holiday_combined.txt", "data/AR/Analysis_promotion_inappropriate_holiday_combined_2.txt")
]

cwd = os.getcwd()

for f1_rel, f2_rel in pairs:
    f1 = os.path.join(cwd, f1_rel)
    f2 = os.path.join(cwd, f2_rel)
    
    # Long path handling
    if os.name == 'nt':
        if len(f1) > 250 and not f1.startswith('\\\\?\\'): f1 = '\\\\?\\' + f1
        if len(f2) > 250 and not f2.startswith('\\\\?\\'): f2 = '\\\\?\\' + f2

    if os.path.exists(f1) and os.path.exists(f2):
        try:
            with open(f1, 'r', encoding='utf-8', errors='ignore') as file1:
                content1 = file1.read()
            with open(f2, 'r', encoding='utf-8', errors='ignore') as file2:
                content2 = file2.read()
            
            if content1 == content2:
                print(f"MATCH: {f1_rel} == {f2_rel}")
            else:
                print(f"DIFF:  {f1_rel} != {f2_rel}")
                print(f"       Lengths: {len(content1)} vs {len(content2)}")
        except Exception as e:
            print(f"Error comparing {f1_rel} and {f2_rel}: {e}")
    else:
        print(f"Skipping pair, file not found: {f1_rel} or {f2_rel}")

