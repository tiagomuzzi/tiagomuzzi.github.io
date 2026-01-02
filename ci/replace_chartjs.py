#script to replace local Chart.js path with CDN path in all .html files

import pathlib
import re

# Find all .html files recursively in the current directory and subdirectories
files = [str(p) for p in pathlib.Path(".").rglob("*.html")]

old = "/chartjs/Chart.bundle.min.js"
new = "https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.6.0/Chart.bundle.min.js"

for file_path in files:
    path = pathlib.Path(file_path)
    if not path.exists():
        print(f"File not found: {file_path}")
        continue
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()
    if old in html:
        pattern = r"file://.*?" + re.escape(old)
        html = re.sub(pattern, new, html)
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Fixed Chart.js path in: {file_path}")