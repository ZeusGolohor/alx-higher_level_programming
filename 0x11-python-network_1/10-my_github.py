#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status.
"""
import requests
import sys
from requests.auth import HTTPBasicAuth


def run():
    url = "https://api.github.com/user"
    user = sys.argv[1]
    pwd = sys.argv[2]
    basic = HTTPBasicAuth(user, pwd)
    req = requests.get(url, auth=(user, pwd))
    print(req.json().get('id'))


if __name__ == "__main__":
    run()
