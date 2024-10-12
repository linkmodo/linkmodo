def main():
    hello()
    helloTo()
    returnFive()
    square(3)

def hello():
    print('hello COP 1047!')

def helloTo(student_name): #name of variable inside ()
    print(f'hello to {student_name}')
    print(f'your number is {result}')

def returnFive():
    return 5

def square(number):
    square_result = number * number
    return square_result

# call the function
hello()

# call function helloTo
# helloTo('Li')

# call returnFive function
result = returnFive()
print(result)

# call square function
result = square(3)
print(f'The square of 3 is {result}')