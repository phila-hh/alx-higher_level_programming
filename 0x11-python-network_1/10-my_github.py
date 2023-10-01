#!/usr/bin/python3
"""
This script takes your GitHub credentials (username and password) and
uses the GitHub API to display your id
"""


from sys import argv
import requests


if __name__ == "__main__":
    user_info = (argv[1], argv[2])
    req = requests.get("https://api.github.com/user", auth=user_info)
    print(req.json().get("id"))
