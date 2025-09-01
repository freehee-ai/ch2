# 문자열 만들기
print('hello')

# 문자열 자르기
print('hello'[0])
print('hello'[1])

# index 란? 문자의 위치
# 무조건 0부터 시작이며 연속적
# [index] => 문자 하나만 추출
# [index 시작: index 끝] => 범위로 추출 ***끝번호포함X***
print('hello'[0:2])
print('hello'[2:5])
print('hello'[2: ])
print('hello'[ :2])
print('hello'[ : ])

# 문자열의 길이를 구하는 함수 : len
print(len('aaa'))