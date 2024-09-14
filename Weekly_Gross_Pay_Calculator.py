# Design a program for Weekly Gross Pay Calculation

hours_worked = float(input('Enter hours worked:'))
hourly_pay_rate = float(input('Enter hourly pay rate:'))

# Process

gross_pay = hours_worked * hourly_pay_rate

# Output

print(f'The weekly gross pay is: ${gross_pay:.2f}!') #Format with f function and {}, two decimals using '.xf'

print('The gross pay is: $' + str(gross_pay)) #Alternative method for string display formating

print('The gross pay is: $', gross_pay, sep='')