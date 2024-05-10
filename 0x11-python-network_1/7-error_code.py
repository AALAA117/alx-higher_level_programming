#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response
"""
import requests
from requests.exceptions import HTTPError
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)
    except HTTPError as err:
        print("Error code: {}".format(err.response.status_code))
