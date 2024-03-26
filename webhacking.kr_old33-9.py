import requests
import hashlib

url = "https://webhacking.kr/challenge/bonus-6/nextt.php"

answer =""
for i in range(97,123,2):
    answer += chr(i)

re_get = {'ans':answer}

response = requests.get(url,params=re_get) #params -> GET 요청에 대한 매개변수

print(response.text)