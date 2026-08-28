
from pathlib import Path
path = Path("data/mony.txt")
path.parent.mkdir(exist_ok=True)
path.write_text("Hello from python")
print("File created")