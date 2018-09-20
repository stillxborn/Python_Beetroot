

meal_cost = float(input("Enter the price of the meal: " ))

price_with_tax = meal_cost / 100 * 18
price_with_tips = meal_cost / 100 * 7

overal_price = meal_cost + price_with_tax + price_with_tips

print("The tax is", price_with_tax, "$")
print("The tips is", price_with_tips, "$")
print("The tax and tips is", price_with_tips + price_with_tax, "$")
print("The totall bill is", overal_price, "$")
