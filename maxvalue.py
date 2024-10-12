# This function detect max value, receives two values
def max(num1, num2): # can be a or b or x or y
    max = 0

    if num1 > num2:
        max = num1
    elif num2 > num1:
        max = num2
    return max

def main():
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))

    # call function
    result = max(number1, number2)

    print(f'The max value of the {result}: \t Number 1 is {number1} and Number 2 is {number2}')

main()