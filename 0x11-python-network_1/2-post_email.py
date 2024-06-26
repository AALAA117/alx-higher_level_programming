#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response
"""
from urllib.request import urlopen, Request
from urllib.parse import urlencode
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    querystring = {"email": argv[2]}
    req = Request(url, urlencode(querystring).encode())
    with urlopen(req) as response:
        body = response.read().decode("utf-8")
    print(body)
