#!/usr/bin/python3
"""
bu modul verilmis URL e sorgu gonderir , HTTP xetalarini idare edir
ve cavabin body hissesini cap edir
"""
import sys
import urllib.request
import urllib.error


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
