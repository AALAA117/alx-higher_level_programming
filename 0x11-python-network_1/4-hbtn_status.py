#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""
import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    req = requests.get(url)
    if isinstance(req.content, bytes):
        content = req.content.decode("utf-8")
    else:
        content = req.content
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
