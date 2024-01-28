#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status.
"""
import requests
import sys


def run():
    url = "http://0.0.0.0:5000/search_user"
    user = sys.argv[1]
    if (len(user) == 0 or user is None):
        user = ""
    req = requests.post(url, data={'q': user})
    try:
        j = req.json()
        if (len(j) > 0):
            print("[{}] {}".format(j["id"], j["name"]))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    if (len(sys.argv) - 1 > 0):
        run()
    else:
        print("No result")
