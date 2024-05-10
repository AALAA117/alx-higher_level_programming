#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    querystring = {"email": argv[2]}
    respond = requests.post(url, querystring)
    print(respond.content)
