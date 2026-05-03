#!/usr/bin/python3
"""
bu modul 'requests' paketi vasitesiile URL den statusu goturur
"""
import requests


if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    r = requests.get(url)

    print("Body response:")
    # requests.get().text bizə birbaşa string (str) qaytarır
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
