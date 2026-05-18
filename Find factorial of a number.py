#Find factorial of a number

number = int(input())

factorial = 1

while number > 0:
    factorial = factorial * number
    number -= 1
print (factorial)
