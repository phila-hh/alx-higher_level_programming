#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL and
displays the value of the variable X-Request-Id in the response header
"""


from sys import argv
import requests


if __name__ == "__main__":
    print(requests.get(argv[1]).headers.get("X-Request-Id"))
