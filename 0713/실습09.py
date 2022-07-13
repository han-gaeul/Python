students = ['이영희', '김철수', '이영희', '조민지', '김철수', '조민지', '이영희', '이영희']

# n = sorted(students)

# print(n)

# if n in students:
#     n == '이영희'


def vote(students):
    count = 0
    for i in students:
        if i == '이영희':
            count += 1
    return count

print(vote(students))