#!/usr/bin/python3
"""
Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/user"
    response = requests.get(url, auth=HTTPBasicAuth(argv[1], argv[2]))
    try:
        id_user = response.json()
        print(id_user.get("id"))
    except Exception:
        print("None")
