#!/bin/bash
# This script takes a URL as input, sends a GET request to the URL with a header X-School-User-Id, and displays the body of the response
curl -s -H "X-School-User-Id: 98" "$1"
