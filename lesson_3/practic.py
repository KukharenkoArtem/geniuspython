# Умовні конструкції
# Task 1

valid_password = "password123"
password = str(input("Введіть пароль: "))
if password == valid_password:
    {
        print("Ви увійшли в систему.")
    }
else:
    {
        print('Неправильний пароль.')
    }


# Task 2

index_of_days = {
    1: 'Понеділок',
    2: 'Вівторок',
    3: 'Середа',
    4: 'Четвер',
    5: 'Пʼятниця',
    6: 'Субота',
    7: 'Неділя'
}

index = int(input("Введіть номер дня тижня: "))
if index < 1 or index > 7:
    print("Помилка! Введено невірний номер. Спробуйте ще раз. (від 1 до 7)")
else:
    print(index_of_days[index])


# Цикли
# Task 1

number = int(input('Введіть число для запису таблиці множення: '))
a = 1
while a <= 10:
    print(f'{number} * {a} =  {number*a}')
    a += 1


# Task 2

numbers = [1, 6, 4, 3, 7, 9]
sum = 0
for i in numbers:
    sum = sum+i
print(sum)

# Task 3

number_2 = int(
    input('Введіть натуральне число для обчислення його факторіала: '))
fact = 1
while number_2 >= 1:
    fact = fact * number_2
    number_2 -= 1
print(fact)

# Task 4
b = 0
list_of_even_numbers = []
while b <= 50:
    if b % 2 == 0:
        list_of_even_numbers.append(b)
    b += 1
print(list_of_even_numbers)
