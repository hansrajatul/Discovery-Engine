def get_users():
    users = []
    with open("/etc/passwd") as f:
        for line in f:
            parts = line.strip().split(":")
            users.append({
                "username": parts[0],
                "uid": parts[2],
                "shell": parts[6]
            })
    return users
