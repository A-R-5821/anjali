price=float(input("how much did you pay?"))
print("price is"+ str(price))
if price >= 1.00:
    tax = .07
else:
    tax = 0
print("Tax rate is:" + str(tax))
