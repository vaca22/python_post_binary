



import json
import time
import hashlib
import requests
import random
import string











if __name__ == '__main__':
    print('PyCharm')
    header = {
        "Content-Type": "application/json; charset=UTF-8",
        "filename": "gaga.txt"
    }
    url = "http://106.13.194.65:9001/post"
    with open('./gaga.txt', 'rb') as f:
        data = f.read()
    resp = requests.post(url, data=data, headers=header)