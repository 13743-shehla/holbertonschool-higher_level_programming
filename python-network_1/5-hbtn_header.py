#!/usr/bin/python3
"""
bu modul 'requests' paketi vaistesile arqument kimi verilen URLe
sorgu gonderir ve header deki 'X-Request-Id' deyerinin cap edir
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    
    r = requests.get(url)
    
    request_id = r.headers.get('X-Request-Id')
    
    print(request_id)
