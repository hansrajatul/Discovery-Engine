import requests
from collectors.users import get_users
from collectors.groups import get_groups
from collectors.sudo import get_sudoers

BACKEND_URL = "http://backend:8000/ingest/linux"

def main():
    data = {
        "server": "linux-host",
        "users": get_users(),
        "groups": get_groups(),
        "sudo": get_sudoers()
    }

    response = requests.post(BACKEND_URL, json=data)
    print(response.text)

if __name__ == "__main__":
    main()
