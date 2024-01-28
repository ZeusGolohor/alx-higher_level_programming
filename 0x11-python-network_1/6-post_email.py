#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status.
"""
import requests
import sys


def run():
    url = sys.argv[1]
    data = {'email': sys.argv[2]}
    req = requests.post(url, data=data)
    print(req.text)


if __name__ == "__main__":
    run()
