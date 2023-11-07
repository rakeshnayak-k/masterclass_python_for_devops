num1 = int(input('Enter 1st Number: '))
num2 = int(input('Enter 2nd Number: '))
choice = input("Enter a Operation ( + - * / ) : ")

if choice == "+":
    sum = num1 + num2
    print('Sum of Two Numbers: ', sum)
elif choice == "-":
    diff = num1 - num2
    print('Subtraction of Two Numbers: ', diff)
elif choice == "*":
    mul = num1 * num2
    print('Multiplication of Two Numbers: ', mul)
elif choice == "/":
    div = num1 / num2
    print('Division of Two Numbers: ', div)
else:
    print('Invalid Choice')


