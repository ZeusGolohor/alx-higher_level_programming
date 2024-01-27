#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status.
"""
import requests
import sys


def run():
    url = sys.argv[1]
    req = requests.get(url)
    if (req.status_code < 400):
        print(req.text)
    else:
        print("Error code: {}".format(req.status_code))


if __name__ == "__main__":
    run()
