text = 'apple'

reversed_str = text[::-1]
print(f'{reversed_str}')



reversed_str = ''

for i in text:
    reversed_str = i + reversed_str
print(f'{reversed_str}')