#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""

import requests

res = requests.get("https://alx-intranet.hbtn.io/status")
print("Body response:")
print(f"\t- type: {type(res.text)}")
print(f"\t- content: {res.text}")
