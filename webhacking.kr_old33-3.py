import requests

url="https://webhacking.kr/challenge/bonus-6/33.php"

old_33_3 = {"myip": "220.66.156.120"}

re_post = requests.get(url,params=old_33_3) #params -> get대한 매개변수

print(re_post.text)