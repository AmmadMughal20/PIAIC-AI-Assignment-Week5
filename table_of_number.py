# Program to print a table of user entered number upto 10

user_input = input('Enter your number: ')
for n in range(1, 11):
    print(f'{user_input} x {n} = ' + str(int(user_input)*n))