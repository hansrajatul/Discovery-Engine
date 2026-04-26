def get_groups():
    groups = []
    with open("/etc/group") as f:
        for line in f:
            parts = line.strip().split(":")
            groups.append({
                "group": parts[0],
                "members": parts[3].split(",") if parts[3] else []
            })
    return groups
