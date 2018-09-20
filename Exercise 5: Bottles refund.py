

Small_bottle_deposit = 0.10
Big_bottle_deposit = 0.25

small = int(input("How many smal bottes do you have? : " ))
big = int(input("How many big bottes do you have?: " ))

refund = small * Small_bottle_deposit + big * Big_bottle_deposit

print("Your total redund will be $%.2f." % refund)