#!/bin/bash
# This script takes in a URL, sends a GET request to the URL,
# and displays the body of the response

response=$(curl -s -w "%{http_code}" "$1")

if [ "$response" -eq 200 ]; then
	curl -s "$1" | sed -n '/<body>/,/<\/body>/p'
fi
