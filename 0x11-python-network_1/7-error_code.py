#!/usr/bin/python3
"""Python script that takes in a URL,
ends a request to the URL and displays the body of the response"""

import requests
import sys

if __name__ == "__main__":
    res = requests.get(sys.argv[1])
    if res.status_code >= 400:
        print(f"Error code: {res.status_code}")
    else:
        print(res.text)
