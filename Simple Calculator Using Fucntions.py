def add_numbers(num1, num2):
    result = num1 + num2
    return result

def sub_numbers(num1, num2):
    result = num1 - num2
    return result

def mul_numbers(num1, num2):
    result = num1 * num2
    return result

def div_numbers(num1, num2):
    result = num1 / num2
    return result

def power(num1, num2):
    result = num1 ** num2
    return result

def print_result(opt, numb1, numb2, totalResult): # provide info for options selected and numbers entered
    if opt == 1:
        print (f'The addition of {numb1} and {numb2} is: {totalResult}')
    elif opt == 2:
        print (f'The subtraction of {numb1} and {numb2} is: {totalResult}')
    elif opt == 3:
        print (f'The multiplication of {numb1} and {numb2} is: {totalResult}')
    elif opt == 4:
        print (f'The division of {numb1} and {numb2} is: {totalResult}')
    elif opt == 5:
        print (f'The power of {numb1} and {numb2} is: {totalResult}')

def main():
    number1 = number2 = 0
    totalResult = 0
    print('Menu')
    print('1. Add numbers')
    print('2. Subtract numbers')
    print('3. Multiple numbers')
    print('4. Divide numbers')
    print('5. "Power of"')

    option = int(input('Enter your choice: '))
    number1 = int(input('Enter first number: '))
    number2 = int(input('Enter second number: '))

    if option == 1:
        totalResult = add_numbers(number1, number2)
    elif option == 2:
        totalResult = sub_numbers(number1, number2)
    elif option == 3:
        totalResult = mul_numbers(number1, number2)
    elif option == 4:
        totalResult = div_numbers(number1, number2)
    elif option == 5:
        totalResult = power(number1, number2)

    # call function to print_result
    print_result(option, number1, number2, totalResult)

main()

