# Списки
# Task 1

lis_1 = [2, 5, 6, 8, 1]
lis_1.extend([10, 20])
print(lis_1)
lis_1.pop(-2)
print(lis_1)


# Task 2

lis_2 = [2, 5, 7, 11, 23, 45]
sum = 0
for i in lis_2:
    sum += i
print(sum)

# Task 3

lis_3 = [3, 5, 7, 8, 2, 11]
for i in range(len(lis_3)):
    lis_3[i] *= 2
print(lis_3)
