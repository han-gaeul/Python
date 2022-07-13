# 주어진 문자열 word가 주어질 때
# 해당 단어에서 'a'를 모두 제거

# 변수 result 선언
# while문보다 for문이 적절
# for문은 하나를 끝까지 반복

# if 단어가 a 일때..


word = 'apple'
# 반복! for문

# for char in 'apple':
#     # 만약 a일 때
#     if char == 'a':
#         # 반복문에서 아무것도 안하고 넘어가기
#         # countinue
#         print('안녕')


result = ''
for char in 'apple':
    # 만약 a가 아닐 때
    if char != 'a':
        result = result + char
        # 반복문에서 아무것도 안하고 넘어가기
        # countinue
print(result)


        
# for char in 'apple':
#     # 만약 a가 아닐 때
#     if char != 'a':
#         print(char)