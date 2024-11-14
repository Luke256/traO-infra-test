import subprocess
from config import IS_REMOTE

def stop_instance():
    if IS_REMOTE:
        subprocess.run(["sudo", "shutdown", "-h", "now"])