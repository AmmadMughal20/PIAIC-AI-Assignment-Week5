#Program to print sum of list elements
from random import randrange
numbers = []
for i in range (1, 101):
    numbers.append(randrange(1,100))

sum = 0

for i in range(0, len(numbers)):
    sum += numbers[i]

print(f'The numbers are: {numbers}')
print(f'The sum is: {sum}')
