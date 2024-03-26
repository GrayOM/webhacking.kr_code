import requests
import hashlib

url = "https://webhacking.kr/challenge/bonus-6/ipt.php"
address = '127.0.0.1'

re_get = { 'addr' : address}

response = requests.get(url,params=re_get) #params -> GET 요청에 대한 매개변수

print(response.text)