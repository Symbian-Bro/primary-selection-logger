import os
import subprocess

log_file_path = os.path.expanduser("~/.log_primary/log_primary.txt")

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