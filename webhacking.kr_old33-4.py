import requests

url="https://webhacking.kr/challenge/bonus-6/l4.php"

l4 = {"password":"b73fe13acccc67c1ffcfa5f3e13bfaaa"} #현재 시간에 대한 MD5 인코딩을 넣어주세요 안된다면 MD5 인코딩 사이트를 바꾸세요
                                                        #안되는 사이트도 간혹 있습니다.

re = requests.get(url,params=l4) #params -> GET 요청에 대한 매개변수

print(re.text)