# numbers = [4, 6, 10, -8, 5]

# for i in range(len(numbers)):
#     numbers[i] = numbers[i] * 2

# print(numbers)


def test(num1,num_list):
    total = 0
    for i in num_list:
        total = total + i * 100
    return num1 + total

print(test(3, [4,5,6]))
        