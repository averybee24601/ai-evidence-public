#!/usr/bin/env python3
"""
Fix the text messages case to show both screenshots
"""

# Read the file
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define the old text to find
old_text = """                {
                    id: 'c8', cat: 'discrimination', title: 'Dismissive Text Messages',
                    evidence: 'data/Analyzed files/text.png',
                    report: 'data/AR/Analysis of text.png.txt',
                    type: 'image',
                    profiles: ['Tiffany Fixter', 'Juliana']
                },"""

# Define the new text to replace it with
new_text = """                {
                    id: 'c8', cat: 'discrimination', title: 'Dismissive Text Messages (Complete Conversation)',
                    evidenceFiles: [
                        'data/Analyzed files/text.png',
                        'data/Analyzed files/text 2 dismissive attitude - Copy.png'
                    ],
                    report: 'data/AR/Analysis of text 2 dismissive attitude - Copy.png.txt',
                    type: 'unified-images',
                    profiles: ['Tiffany Fixter', 'Avery Becker', 'Juliana']
                },"""

# Replace
if old_text in content:
    content = content.replace(old_text, new_text)
    print("✓ Found and replaced text messages configuration")
else:
    print("✗ Could not find the exact text to replace")
    print("Searching for similar patterns...")
    if "'c8'" in content and "Dismissive Text Messages" in content:
        print("Found c8 and title, but exact match failed")
        print("You may need to edit manually")
    
# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done!")
