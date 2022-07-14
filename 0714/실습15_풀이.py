# 
word = 'bbbbb'

# 1. for-else 풀이
# 문자로 순회하는 것이 아니라
# 인덱스로 접근해서 사용
# 원하는 숫자는 0, 1, 2, 3, 4, 5
# 숫자를 얻는 방법은 range(len(word)) -> range(6) -> 0 ~ 5

for idx in range(len(word)):
    #print(idx, word[idx])
    # 알파벳이 a 일 때
    if word[idx] == 'a':
        print(idx)
        break
# for문을 다 돌았다는 뜻은
# 한번도 break에 안 걸렸다
# 즉, a는 없었다.
else:
    print(-1)



# 2. 

# a가 있었는지 없었는지 (boolean)

is_a = False

for idx in range(len(word)):
    if word[idx] == 'a':
        print(idx)
        is_a = True
        break

if is_a == False:
#if not is_a:
    print(-1)