#!/usr/bin/python3
"""
displays the value of the X-Request-Id variable
found in the header of the response.
"""
from urllib.request import urlopen, Request
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    with urlopen(url) as response:
        request_id = response.headers["X-Request-Id"]
    print(request_id)
