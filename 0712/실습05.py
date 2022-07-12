numbers = [3, 10, 20]

result = 0

# for val in numbers:
#     result += val
# print(result/len(numbers))


cnt = 0

for i in numbers:
    result += i
    cnt += 1

avg = result / cnt

print(avg)
