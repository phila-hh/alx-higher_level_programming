#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response
"""


from urllib import request
from sys import argv


if __name__ == "__main__":
    with request.urlopen(argv[1]) as webpage:
        print(webpage.getheader("X-Request-Id"))
