#Program to print elements of list greater than 40

from random import randrange
list = []
for i in range(1,101): 
    list.append(randrange(1,100))

filteredlist = []
for i in range(0,len(list)):
    filteredlist.append(list[i]) if list[i] > 40  else exit

print('Numbers greater than 40 are: ' + str(len(filteredlist)))
print(filteredlist)
print('Complete list is: ')
print(list)
