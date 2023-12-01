#!/bin/bash
# This script takes in a URL, sends a GET request to the URL, and displays the
#	body of the response

if [[ $# -eq 1 ]]
then
	curl -sGL "$1"
fi
