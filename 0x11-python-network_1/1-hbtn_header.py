#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status.
"""
import urllib.request
import sys


def run():
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        data = response.info()
        print(data.get("X-Request-Id"))


if __name__ == "__main__":
    run()
