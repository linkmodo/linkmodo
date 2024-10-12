#calculate my profit for resaling the motorcycle keyblanks

originalCost: float = 19.47 / 18
resalesPrice: float = 10.00
shippingCost: float = 3.85

profit = resalesPrice - shippingCost - originalCost
totalProfit = profit * 18 - 20

print(f'My profit for each sale of the key blank is ${profit:.2f}')
print(f'My total profit for selling all key blanks are ${int(totalProfit)}')

