#!/bin/bash
# a script to count the size of curl request.
curl -s "$1" | wc -c
