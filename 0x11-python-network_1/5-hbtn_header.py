#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status.
"""
import requests
import sys


def run():
    url = sys.argv[1]
    req = requests.get(url)
    print(req.headers.get("X-Request-Id"))


if __name__ == "__main__":
    run()
