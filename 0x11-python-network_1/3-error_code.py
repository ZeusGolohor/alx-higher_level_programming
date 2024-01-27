#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status.
"""
import urllib.request
import sys


def run():
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read()
            print(data.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))


if __name__ == "__main__":
    run()
