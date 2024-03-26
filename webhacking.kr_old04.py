import base64

# 문자열을 Base64로 20번 인코딩하는 함수
def base64_encode_twenty_times(string):
    # 문자열을 UTF-8로 인코딩하여 bytes로 변환
    encoded_string = string.encode('utf-8')
    
    # 20번 반복하여 인코딩
    for _ in range(20):
        encoded_string = base64.b64encode(encoded_string)  # Base64 인코딩
        
    # bytes를 다시 문자열로 디코딩하여 반환
    return encoded_string.decode('utf-8')

# 문자열 치환 함수
def custom_replace(string):
    # 각 문자에 대한 치환 규칙 정의
    replacements = {
        '1': '!',
        '2': '@',
        '3': '$',
        '4': '^',
        '5': '&',
        '6': '*',
        '7': '(',
        '8': ')'
    }

    # 문자열을 순회하며 치환된 결과 생성
    replaced_string = ''
    for char in string:
        # 문자가 규칙에 맞는 경우 치환, 그렇지 않으면 그대로 유지
        replaced_string += replacements.get(char, char)
    
    return replaced_string

# 'admin'과 'nimda'를 Base64로 20번 인코딩하고 치환 적용
encoded_admin = base64_encode_twenty_times('admin')
encoded_nimda = base64_encode_twenty_times('nimda')

# 치환된 결과 출력
encoded_admin_replaced = custom_replace(encoded_admin)
encoded_nimda_replaced = custom_replace(encoded_nimda)

print("'admin':", encoded_admin_replaced)
print("'nimda':", encoded_nimda_replaced)
