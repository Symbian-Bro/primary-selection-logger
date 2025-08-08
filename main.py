import os
import subprocess
import time

log_file_path = os.path.expanduser("~/.log_primary/log_primary.txt")
os.makedirs(os.path.dirname(log_file_path), exist_ok=True)

def get_primary_selection():

    try:
        result = subprocess.run(
            ["xclip", "-o", "-selection", "primary"],
            capture_output=True,
            text=True
        )
        text = result.stdout.strip()
        return text
    except Exception:
        return ""

last_selection = None

while (True):
    latest_selection = get_primary_selection()
    if (latest_selection != last_selection):
        last_selection = latest_selection
        with open(log_file_path, "ab") as f:
            f.write((selection + "\n").encode("utf-8"))

    time.sleep(0.2)