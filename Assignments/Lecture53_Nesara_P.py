def VatCalculate(totalPrice):
    result = totalPrice + (totalPrice*7/100)
    return result

totalPrice = int(input("Total price ="))
print(VatCalculate(totalPrice))