import re

print("📬 Let's extract email addresses from a .txt file!")

file_path = input("Enter the path to your .txt file: ").strip()
save_path = input("Where should we save the found emails? (output.txt): ").strip() or "output.txt"

with open(file_path, 'r') as file:
    content = file.read()

emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}', content)

with open(save_path, 'w') as out:
    out.write("\\n".join(emails))

print(f"✅ Found and saved {len(emails)} email(s) to '{save_path}'.")
