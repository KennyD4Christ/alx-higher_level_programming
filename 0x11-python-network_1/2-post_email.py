#!/usr/bin/python3
"""
Takes in a URL and an email, sends a POST request to the passed URL with the
email as a parameter, and displays the body of the response (decoded in utf-8).
"""

import sys
from urllib import parse, request


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <URL> <email>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    data = parse.urlencode({'email': email}).encode('utf-8')
    req = request.Request(url, data=data, method='POST')

    try:
        with request.urlopen(req) as response:
            body = response.read().decode('utf-8')
            print(body)
    except request.URLError as e:
        print("Error:", e.reason)
