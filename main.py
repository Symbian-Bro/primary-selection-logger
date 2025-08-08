import os
import subprocess
import time
from datetime import datetime

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
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    if (latest_selection != last_selection):
        last_selection = latest_selection
        stamp = f"{timestamp} {selection}\n"
        with open(log_file_path, "ab") as f:
            f.write((stamp + "\n").encode("utf-8"))

    time.sleep(0.1)