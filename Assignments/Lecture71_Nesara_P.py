menuList = []
priceList = []
total = 0
def showBill():
    print("----- My Food -----")
    for number in range(len(menuList)):
        print(menuList[number],priceList[number])
    print("Total :", total , "THB")

while True:
    menuName = input("Please Enter Menu :")
    if(menuName.lower() == "exit"):          #อย่าลืมคิดเคสที่จะเกิดขึ้น
        break
    else:
        menuPrice = int(input("Price :"))
        total += menuPrice
        menuList.append(menuName)
        priceList.append(menuPrice)
showBill()