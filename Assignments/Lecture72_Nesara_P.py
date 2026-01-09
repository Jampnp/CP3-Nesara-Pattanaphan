menuList = []
total = 0
def showBill():
    print("----- My Food -----")
    for number in range(len(menuList)):
        print(menuList[number][0],menuList[number][1])
    print("Total :", total , "THB")

while True:
    menuName = input("Please Enter Menu :")
    if(menuName.lower() == "exit"):          
        break
    else:
        menuPrice = input("Price :")
        total += int(menuPrice)
        menuList.append([menuName,menuPrice])

showBill()