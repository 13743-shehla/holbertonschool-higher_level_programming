#!/usr/bin/python3
"""
Module that sends a request to a URL and displays the body of the response.
Handles HTTP errors by printing the status code if it's >= 400.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)

    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
