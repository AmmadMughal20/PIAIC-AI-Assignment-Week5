#Program to print the minimum value in a list
from random import randrange

numbers = []

for i in range(1,101):
    numbers.append(randrange(1,100))

minimum = 100
i = 0
while i < len(numbers):
    if minimum > numbers[i]:
        minimum = numbers[i]
    i += 1 
    
print(f'The list is: {numbers}')
print(f'The minimum value is: {minimum}')