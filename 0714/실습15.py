word = 'banana'
# str = 'a'
# list = []

# for i, n in enumerate(word):
#     if(n == str):
#         list.append(i)
#         print(i)
#         break
#     else:
#         if(n != str):
#             print(-1)

for i in range(len(word)):
    if word[i] == 'a':
        print(i)
        break

    if 'a' not in word:
        print(-1)
        break




word = 'HappyHacking'
str = 'a'
list = []

for i, n in enumerate(word):
    if(n == str):
        list.append(i)

print(list)