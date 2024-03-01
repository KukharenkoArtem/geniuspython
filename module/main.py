import calculator
a = float(input('Enter the first number: '))
b = float(input('Enter the second number: '))
operation = str(input("Enter the operation (add,subtract,multiply,divide): "))
if operation == 'add':
    print(calculator.add(a, b))
elif operation == 'subtract':
    print(calculator.subtract(a, b))
elif operation == 'multiply':
    print(calculator.multiply(a, b))
elif operation == 'divide':
    print(calculator.divide(a, b))
else:
    print('Invalid operation')
