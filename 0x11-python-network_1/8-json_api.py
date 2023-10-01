#!/usr/bin/python3
"""
This script takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""


from sys import argv
import requests


if __name__ == "__main__":
    info = {"q": argv[1] if len(argv) > 1 else ""}
    req = requests.post("http://0.0.0.0:5000/search_user", data=info)
    try:
        json = req.json()
        if json:
            print("[{}] {}".format(json.get("id"), json.get("name")))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
