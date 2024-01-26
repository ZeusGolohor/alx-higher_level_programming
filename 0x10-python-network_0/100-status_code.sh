#!/bin/bash
# Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -s --head "$1" | grep -i "HTTP/1.1" | cut -d ' ' -f 2
