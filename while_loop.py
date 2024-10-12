count = 0
result = 0

while count < 6:   # while is the times the variable is executed
    count = count + 1
    num1 = int(input("Keep entering a number: "))
    result = result + num1
average = result / count

print(f'The result of the numbers is: {result}')
print(f'The average is: {average}')