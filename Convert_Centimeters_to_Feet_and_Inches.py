# Input

print ('[Total Centimeters To Feet and Inches Calculator]')

cm = float(input("Enter Centimeters: "))

# Calculation

total_in = cm * 0.394
total_whole_ft = total_in // 12
total_remaining_in = total_in % 12

# Output
print (f'{cm:.0f} centimeters converts to {total_in:.2f} inches.')
print (f'The total Feet and Inches is: {total_whole_ft:.0f} ft and {total_remaining_in:.2f} in.')
