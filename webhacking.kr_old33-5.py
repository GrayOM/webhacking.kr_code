import requests

url="https://webhacking.kr/challenge/bonus-6/md555.php?imget=1"

post = {'impost':'1'}
cookie ={'imcookie':'1'}

re = requests.post(url,cookies=cookie,data=post) 

print(re.text)
