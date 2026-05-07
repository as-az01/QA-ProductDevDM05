from pathlib import Path
from datetime import datetime

out = Path("/data/hello.txt")

if out.exists():
    current_content = out.read_text()
    print("current content:")
    print(current_content)
else:
    print("file no exist:")

with out.open("a") as f:
    f.write("hello dock {datetime.now()}\n")