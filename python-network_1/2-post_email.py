#!/usr/bin/python3
"""
bu modul verilmis URL e email parametri ile POST sorgusu gonderir
ve serverin cavabini ekrana cap edir
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    values = {'email': email}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)
