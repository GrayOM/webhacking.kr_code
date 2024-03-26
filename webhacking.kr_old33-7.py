import requests
import hashlib

url = "https://webhacking.kr/challenge/bonus-6/wtff.php"
address = '자신의 ip 입력' #.을 뺴야함

re_get = { address : address}

response = requests.get(url,params=re_get) #params -> GET 요청에 대한 매개변수

print(response.text)