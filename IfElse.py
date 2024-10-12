

# String comparison is based on ASCII code numbers

num1 = 5
num2 = 4
name1 = 'Daniel'
name2 = 'Brandon'

if name1 > name2:
    print(f'The name {name1} is greater than name {name2}')

elif name1 < name2:
    print(f'The name {name1} is less than name {name2}')

elif name1 == name2:
    print(f'The name {name1} is equal to {name2}')

elif name1 != name2:
    print(f'The name {name1} is not equal to {name2}')

elif name1 <= name2:
    print(f'The name {name1} is less than {name2}')

elif name1 >= name2:
    print(f'The name {name1} is greater than {name2}')

if num1 == num2:
    print('This is inside num IF')
    print(f'The number {num1} is equal the number {num2}')

else:
    print('This is inside num ELSE')
    print(f'The number {num1} is different than the number {num2}')