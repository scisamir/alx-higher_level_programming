#!/bin/bash
# This script sends a DELETE request to the URL passed as the first argument
#	and displays the body of the response

if [[ $# -eq 1 ]]
then
	curl -s -X DELETE "$1"
fi
