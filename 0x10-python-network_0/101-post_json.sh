#!/bin/bash
# Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -sL -H "Content-Type: application/json" -X POST -d "$(cat "$2")" "$1"