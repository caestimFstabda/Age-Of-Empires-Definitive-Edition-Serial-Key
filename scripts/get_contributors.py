import os
import json

root_dir = os.path.join(os.path.dirname(__file__), "..")
os.chdir(root_dir) # move to root project

print("Getting contributors...")

try:
    import requests
except ImportError:
    os.system("pip install requests")
    import requests

response = requests.get("https://api.github.com/repos/marticliment/WingetUI/contributors?anon=1")

contributors = []
contributorsInfo = []

for contributor in response.json():
    login = contributor.get("login", None)
    if (contributor.get("type") == "User" and login):
        contributors.append(login)
        contributorsInfo.append({
            "name": login,
            "link": contributor.get("html_url"),
            "contributions": contributor.get("contributions"),
        })

output = f"""
# Autogenerated file, do not modify it!!!

contributors = {json.dumps(contributors, indent=2, ensure_ascii=False)}

contributorsInfo = {json.dumps(contributorsInfo, indent=2, ensure_ascii=False)}
"""

contributors_filepath = os.path.normapth(os.path.join(root_dir, "wingetui/data/contributors.py"))
with open(contributors_filepath, "w", encoding="utf-8") as f:
    f.write(output.strip())

print("done!")
