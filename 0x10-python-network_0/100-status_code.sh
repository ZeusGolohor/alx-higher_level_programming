#!/bin/bash
# Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -s --head -w "%{http_code}" -o /dev/null "$1"
