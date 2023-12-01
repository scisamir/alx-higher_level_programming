#!/bin/bash
# This bash script takes in a URL and displays all HTTP methods the server will accept.

if [[ $# -eq 1 ]]
then
	curl -s -I -X OPTIONS "$1" | grep 'Allow' | cut -d ' ' -f 2-
fi
