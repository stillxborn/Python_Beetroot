
deposit_amount=float(input("Enter deposit amount:"))
time=int(input("Enter time duration:"))
rate=float(input("Enter interest rate:"))
def cou_interest(deposit_amount,time,rate):
    return (deposit_amount * (1 + (float(rate) / 100)) ** time)

amount =cou_interest(deposit_amount,time,rate)
compound_interest=amount-deposit_amount;
print("Total amount is :",amount, "$")
print("Compound interest:- ",compound_interest, '$')



