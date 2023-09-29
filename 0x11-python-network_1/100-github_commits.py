#!/usr/bin/python3
"""Python script that list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
"""

import requests
import sys

if __name__ == "__main__":
    try:
        repo = sys.argv[1]
        owner = sys.argv[2]
        url = f"https://api.github.com/repos/{owner}/{repo}/commits"

        res = requests.get(url)

        for i in range(10):
            commit = res.json()[i]
            sha = commit.get("sha")
            name = commit.get("commit").get("author").get("name")
            print(f"{sha}: {name}")
    except Exception:
        pass
