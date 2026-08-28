from pathlib import Path

file_path = Path("data/mony.txt")

if file_path.exists():
    print("Print to read")
else:
    print("File is missing")


