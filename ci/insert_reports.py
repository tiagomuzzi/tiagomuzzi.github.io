import sys

#source_folder
root_folder = "../"
sys.path.append(root_folder)
index_path = "index.html"

# Define your placeholders and their corresponding iframe HTML
replacements = {
    "<!--REPORT_IFRAME-->": '<iframe src="monthly_expenses_over_time.html" width="100%" height="600" style="border:none;"></iframe>',
    "<!--APRIL_PIECHART-->": '<iframe src="reports/april/april_piechart.html" width="100%" height="400" style="border:none;"></iframe>',
    # Add more placeholders and iframes as needed
}

with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

for placeholder, iframe_code in replacements.items():
    if placeholder in html:
        html = html.replace(placeholder, iframe_code)
        print(f"Replaced {placeholder} with iframe {iframe_code}.")

# Optionally, fallback logic for missing placeholders can be added here

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html)