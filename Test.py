def add(x,y): 
    return x + y

#print(add(8,9))
#print(add(2,2))
#print(add(0, 4))

def subtract(x,y):
    return x - y

#print(subtract(9,3))
#print(subtract(2,9))

def multiply(x,y):
    return x * y

#print(multiply(8,-7))

def divide(x,y):
    if y == 0:
        return 'Error, you cannot divide by 0'
    else:
        return x/y

#print(divide(8,9))
#print(divide(5,0))

def calculator():
    print('Simple Calculator')
    print('Select Opreation: Add, Subtract, Multiply, Divide')

    #Get user input
    operation = input('Enter the operation you want: Add, Subtract, Multiply, Divide:')

    if operation.lower() not in ['add', 'subtract', 'multiply', 'divide']:
        print('Error, input not defined')
        return

    try:
        number1 = float(input('Enter first number:'))
        number2 = float(input('Enter second number:'))
    except ValueError:
        print('Invalid Input')
        return
    
    if operation.lower() == 'add':
        print('Result: ', add(number1, number2))
    elif operation.lower() == 'subtract':
        print('Result: ', subtract(number1, number2))
    elif operation.lower() == 'multiply':
        print('Result: ', multiply(number1, number2))
    elif operation.lower() == 'divide':
        print('Result: ', divide(number1, number2))

calculator()