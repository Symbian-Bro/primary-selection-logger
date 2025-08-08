import os
import subprocess

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