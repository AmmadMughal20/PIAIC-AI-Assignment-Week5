from random import randrange
random_no = randrange(1, 10)
guess1, guess2, guess3 = int(input('Enter your first guess: ')), int(input('Enter your second guess: ')), int(input('Enter your third guess: '))
print(f'You won! The number is {random_no}') if guess1 == random_no or guess2 == random_no or guess3 == random_no else print(f'You lose! The number is {random_no}')
    