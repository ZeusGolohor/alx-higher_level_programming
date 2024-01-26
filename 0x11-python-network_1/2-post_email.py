#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status.
"""
import urllib.request
import sys


def run():
    url = sys.argv[1]
    email = sys.argv[2]
    values = {'email': email}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = url.request.Request(url, data)
    with urllib.request.urlopen(url) as response:
        data = response.read()
        print(data)


if __name__ == "__main__":
    run()
