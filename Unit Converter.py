# input

inches = float(input('Enter inches:'))
feet = float(input('Enter the feet:'))

# calculation

total_inches = inches + feet * 12 # order of operation, 1st (); 2nd *,/,//,%, exp;, 3rd +, -

total_cm = total_inches * 2.54

# display result

print(f'The total length is: {total_cm:.2f}')
print(f'The initial inches {inches:.2f} plus the initial feet {feet:.2f} is {total_cm:.2f}')

# whole division using // and %
