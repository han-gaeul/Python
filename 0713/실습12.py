text = 'apple'

x = text.strip('a')
print(x)

new_text = text.replace('a', '')
print(new_text)

result = text
for str in text:
    if str in 'a':
        result = result.replace(str, '')
print(result)