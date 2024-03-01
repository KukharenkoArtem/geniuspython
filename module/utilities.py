def calculate_average(numbers):
    sum = 0
    for i in numbers:
        sum += i
    print(sum/len(numbers))


def find_max(numbers):
    max = 0
    for i in numbers:
        if i > max:
            max = i
    print(max)
