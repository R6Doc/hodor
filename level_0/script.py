#!/usr/bin/python3

import requests

""" Votes for a specified id """


response = requests.get('http://158.69.76.135/level0.php')
host = "http://158.69.76.135/level0.php"
payload = {'id': '1557', 'holdthedoor': 'submit'}
for i in range(1024):
    req = requests.post(host, payload)
    print("vote: {} status: {}".format(i, response.status_code))
