
import os

def patch_file(path, target, replacement):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Using simple string replace is safer regarding whitespace
    if target in content:
        new_content = content.replace(target, replacement)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Patched {path}")
    else:
        print(f"Target not found in {path}")

# Add script tag
client_path = r'C:\Users\alexp\OneDrive\Desktop\oma\client.html'
master_path = r'C:\Users\alexp\OneDrive\Desktop\oma\master.html'

head_target = '  <script defer src="js/data.js"></script>'
head_replacement = '  <script defer src="js/data.js"></script>\n  <script src="https://cdn.talkjs.com/talk.js"></script>'

patch_file(client_path, head_target, head_replacement)
patch_file(master_path, head_target, head_replacement)
