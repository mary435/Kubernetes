#!/usr/bin/env python
# coding: utf-8

import requests

#url = 'http://localhost:9696/predict'
#url = 'http://localhost:8080/predict'
url = 'http://a0102929f08ac482f95bf847b3c31763-179380389.sa-east-1.elb.amazonaws.com/predict'

data = {'url': 'http://bit.ly/mlbookcamp-pants'}

result = requests.post(url, json=data).json()
print(result)