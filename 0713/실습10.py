numbers = [7, 17, 10, 5, 4, 3, 17, 5, 2, 5]

n1 = numbers.count(5)
print(n1)

def v(numbers):
    count = 0
    for i in numbers:
        if i == 5:
            count += 1
    return count

print(v(numbers))