# Online Purchase Program using Sentinel Looping
# Additional functions include pagination, dictionary creation, list creation
# And keyboard navigation of item ordering page
# Author: Li Fan (with some help from ChatGPT)
# Last updated: 9/28/2024

# Variables
customer_name = ''
option = 0
count = 0  # LCV loop controlled variable
sales_tax = 0.0  # variable used to calculate tax
total = 0.0  # variable to accumulate the total price
total_amount_due = 0.0  # variable to calculate total amount due
ordered_items = []  # list to store and display ordered items

# Constants
SALES_TAX_RATE = 0.0070
SENTINEL = 0

# Item dictionary to store item names and their prices
items = {
    1: ("Smartphone", 249.00),
    2: ("Smartphone case", 39.00),
    3: ("PC Laptop", 1149.00),
    4: ("Tablet", 349.00),
    5: ("Tablet case", 49.00),
    6: ("eReader", 119.00),
    7: ("PC Desktop", 899.00),
    8: ("LED Monitor", 299.00),
    9: ("Laser Printer", 399.00),
    10: ("Mechanical Keyboard", 129.00),
    11: ("Wireless Mouse", 49.00),
    12: ("External SSD (1TB)", 179.00),
    13: ("Gaming Headset", 199.00),
    14: ("Webcam (1080p)", 89.00),
    15: ("USB-C Hub", 69.00),
    16: ("Bluetooth Speakers", 159.00),
    17: ("Wi-Fi Router", 129.00),
    18: ("Docking Station", 249.00),
    19: ("Graphics Card", 549.00),
    20: ("Motherboard", 199.00),
    21: ("Processor (Intel i7)", 329.00),
    22: ("RAM (16GB)", 129.00),
    23: ("Hard Drive (4TB)", 139.00),
    24: ("Power Supply Unit (750W)", 99.00),
    25: ("PC Case", 109.00),
    26: ("Smartwatch", 229.00),
    27: ("VR Headset", 499.00),
    28: ("Portable Projector", 299.00),
    29: ("Wireless Charger", 39.00),
    30: ("Noise Cancelling Headphones", 349.00)
}

# A function to display items with pagination
def display_items(items, start_index=1, items_per_page=10):
    end_index = start_index + items_per_page - 1
    print('Please select the item numbers from the menu:')
    for i in range(start_index, min(end_index + 1, len(items) + 1)):
        item_name, item_price = items[i]
        print(f'{i}. {item_name}    ${item_price:.2f}')
    print('0. Complete my order')

# Input customer name
customer_name = str(input('Please enter your name: '))
print()

# Initialize pagination control variables
start_index = 1
items_per_page = 10  # Set the number of items to display per page

# Loop for user selection with pagination and the option to go back
while True:
    display_items(items, start_index, items_per_page)

    # Determine if there are more pages or a previous page
    if start_index > 1 and len(items) > start_index + items_per_page - 1:
        next_action = input("Enter 'n' for next page, 'p' for previous page, or select an item number: ").strip().lower()
    elif start_index > 1:
        next_action = input("Enter 'p' for previous page or select an item number: ").strip().lower()
    elif len(items) > start_index + items_per_page - 1:
        next_action = input("Enter 'n' for next page or select an item number: ").strip().lower()
    else:
        next_action = input('Select an item number: ').strip().lower()

    if next_action == 'n' and len(items) > start_index + items_per_page - 1:
        start_index += items_per_page  # Move to next page
    elif next_action == 'p' and start_index > 1:
        start_index -= items_per_page  # Move to previous page
    elif next_action.isdigit():
        option = int(next_action)
        if option == SENTINEL:
            break
        elif option in items:
            count += 1
            total += items[option][1]
            ordered_items.append(items[option][0])  # Add ordered item to list
        else:
            print('Invalid selection. Please try again.')
    else:
        print('Invalid input. Please try again.')

# Calculating totals
sales_tax = float(total * SALES_TAX_RATE)
total_amount_due = float(total + sales_tax)

# Print report
print()
print(f'Thank you for ordering with Automated Ordering System, {customer_name}:')
print('------------------------------------------------')
print(f'Total items you\'ve ordered: {count}')

# Display the list of ordered items
if ordered_items:
    print('Items you ordered:')
    for item in ordered_items:
        print(f'- {item}')
else:
    print('No items ordered.')

print(f'Total amount before tax: ${total:.2f}')
print(f'Total sales tax: ${sales_tax:.2f}')
print(f'Your total amount due is: ${total_amount_due:.2f}')
print('------------------------------------------------')
