#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status.
"""
import urllib.request
import sys
import urllib.parse


def run():
    url = sys.argv[1]
    email = sys.argv[2]
    print(url)
    print(email)
    values = {'email': email}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(url) as response:
        data = response.read()
        print(data)


if __name__ == "__main__":
    run()
