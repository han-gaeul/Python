num = -10

# 1. 양수면 그대로
if num >= 0:
    value = num

# 2. 음수면 - 붙여서
else:
    value = -num
print(num, value)

# 조건 표현식 코드
value = num if num >= 0 else -num


# 1. 'if num >=0' ~~ 조건일 때
# 2. 'num' 이 값을
# 3. 'else' 아닐 때는
# 4. '-num' 이거 해