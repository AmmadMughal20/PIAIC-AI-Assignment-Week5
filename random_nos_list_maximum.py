#Program to print the maximum element in a list

from random import randrange

numbers = []
for i in range(1, 101):
    numbers.append(randrange(1,100))

maximum = 0
i = 0
while i < len(numbers):
    if numbers[i] > maximum:
        maximum = numbers[i]
    i+=1
print(f'The list is: {numbers}')
print(f'The maximum is: {maximum}') 