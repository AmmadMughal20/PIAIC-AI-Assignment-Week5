lst1size = int(input('\nWhat is the size of first list? '))
lst2size = int(input('What is the size of first list? '))
list1 = []
list2 = []

print('\nEnter list 1 elements: ')
for i in range(0, lst1size):
    ele = int(input(f'Enter element {i+1} of list 1: '))
    list1.append(ele)
#print(list1)

print('\nEnter list 2 elements: ')
for i in range(0, lst2size):
    ele = int(input(f'Enter element {i+1} of list 2: '))
    list2.append(ele)
#print(list2)

common_elements = []

for x in range(0, len(list1)):
    for y in range(0, len(list2)):
        if list1[x] == list2[y]:
            common_elements.append(list1[x])
            break 
        
print(f'\nThe common elements in lists are: {common_elements}')
