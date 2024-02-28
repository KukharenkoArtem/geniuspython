# Робота з рядками
# Task 1

num_str = 125
num_str = str(num_str)
print(type(num_str))


# Task 2

message = "Hi, my name is Python!"
message = message.replace("y", "0")
message = message.replace("i", "1")
print(message)


# Task 3

split_test = 'This is a split test'
split_test = split_test.split()
print(split_test)
string_join = ' '.join(split_test)
print(string_join)

# Task 4

print(len(string_join))


# Робота зі списками
# Task 1

list_append = [1, 2, 3]
list_append.append(4)
list_append.append(5)
print(list_append)

# Task 2

list_extend = [4, 5, 6]
list_extend.extend([7, 8, 9])
print(list_extend)

# Task 3

print(list_extend.index(6))


# Task 4

print(len(list_append))


# Робота зі словниками
# Task 1

dict_test = {'car': 'Toyota', 'price': '4900', 'where': 'EU'}
print(dict_test['car'])
print(dict_test['where'])

# Task 2

print(dict_test.keys())
print(dict_test.values())

# Task 3

print(dict_test.items())
