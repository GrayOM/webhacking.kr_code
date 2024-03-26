import requests

url_1="https://webhacking.kr/challenge/bonus-6/"

get_hehe = {"get":"hehe"}

re = requests.get(url_1,params=get_hehe) #params -> GET 요청에 대한 매개변수

print(re.text)