#!/usr/bin/python3
"""
Uses GitHub API to display the user id using Basic Authentication.
"""
import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"

    r = requests.get(url, auth=HTTPBasicAuth(username, password))

    try:
        json_data = r.json()
        print(json_data.get('id'))
    except ValueError:
        print("Not a valid JSON")
