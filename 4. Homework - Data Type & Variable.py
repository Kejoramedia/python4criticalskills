"""# 1. EASY CHALLENGE
# 1. Homework: Math operations
a = float(input('Enter first number:'))
b = float(input('Enter second number: '))

print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b}')

# 2. Homework: Student grades
name1 = str(input("Enter the first student's name: "))
id1 = str(input("Enter the first student's ID: "))
grade1 = float(input("Enter the first student's grade: "))
print('\n')
name2 = str(input("Enter the second student's name: "))
id2 = str(input("Enter the second student's ID: "))
grade2 = float(input("Enter the second student's grade: "))
print('\n')
average_grade = (grade1 + grade2) / 2

print(f'{name1}(ID {id1}) got grade: {grade1}')
print(f'{name2}(ID {id2}) got grade: {grade2}')
print(f'Average math grades is {average_grade}')

# 3. Homework: Even and Odd Sum
a, b, c, d, e, f, g, h = map(int, input('Input: ').split())
output1, output2 = a + c + e + g, b + d + f + h

print(f'Output: {output2} {output1}')

# 4. Homework: Special concatenation
a = str(input(''))
b = str(input(''))
c = str(input(''))
print(f'''{a}'{b}"{c}''' * 10)


# MEDIUM CHALLENGE
# 1. Homework: Fibonacci Pattern (Guess Output)

# 2. Homework: Swapping 2 numbers
# a = 15, b = 20
num1, num2 = map(int, input().split())
num3 = num1
num1 = num2
num2 = num3

print(num1, num2)

# Code in pythonic way
num1, num2 = map(int, input().split())

num1, num2 = num2, num1

print(num1, num2)

# HARD CHALLENGE
# 1. Homework: Swapping 3 numbers
# a = 115, b = 20, c = 301
# a = 20, b = 301, c = 115
num1, num2, num3 = map(int, input().split())

num4 = num1
num1 = num2
num2 = num3
num3 = num4

print(num1, num2, num3)

# Code in pythonic way
num1, num2, num3 = map(int, input().split())

num1, num2, num3 = num2, num3, num1

print(num1, num2, num3)

# 2. Homework: Print Me
a, b = map(int, input().split())

eq1 = 2 * a + 1
eq2 = a * a

eqb1 = (b + 1) / 2
eqb2 = 1 - eqb1

ans = eq1 * eqb2 + eq2 * eqb1

print(ans)

# 3. Homework: Sum numbers from 1 to N
N = int(input('N = '))
sumN = (N * (N + 1)) / 2

print(sumN)"""
