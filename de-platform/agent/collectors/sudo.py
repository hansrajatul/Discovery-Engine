import subprocess

def get_sudoers():
    result = subprocess.run(["cat", "/etc/sudoers"], capture_output=True, text=True)
    return result.stdout
