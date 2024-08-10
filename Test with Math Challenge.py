import random
import time

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

def math_challenge():
    print("\n math_challenge")
    score = 0
    start_time = time.time()
    time_limit = 30

    while True:
        if time.time() - start_time > time_limit:
            break

        #Generate Random Math Problem
        num1 = random.randint(1,10)
        num2 = random.randint(1,10) 
        #print(num1, num2)
        operation = random.choice(["+", "-", "*", "/"])

        if operation == "+":
            correct_answer = add(num1, num2)
        elif operation == "-":
            correct_answer = subtract(num1, num2)
        elif operation == "*":
            correct_answer = multiply(num1, num2)
        elif operation == "/":
            correct_answer = divide(num1, num2)

        #Ask User For Answers
        user_answer = input("What's " + str(num1) + "" + str(operation) + "" + str(num2) + "?")

        try:
            user_answer = float(user_answer)
            if user_answer == correct_answer:
                print("Correct")
                score += 1
            else:
                print("Incorrect, The Correct Answer Was " + str(correct_answer))
        except ValueError:
            print("Invalid Input, Please Enter A Number")
    print("Time Is Up, Your Score Is " + str(score))  




def calculator():
    print('Simple Calculator')
    print('Select Opreation: Add, Subtract, Multiply, Divide, Math Challenge')

    #Get user input
    operation = input('Enter the operation you want: Add, Subtract, Multiply, Divide:')

    if operation.lower() not in ['add', 'subtract', 'multiply', 'divide', 'math challenge']:
        print('Error, input not defined')
        return
    if operation.lower() in ['add', 'subtract', 'multiply', 'divide', 'math challenge']:
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
    elif operation.lower() == 'math challenge': 
        math_challenge()
    else:
        print("Invalid Input")
#calculator()
math_challenge()