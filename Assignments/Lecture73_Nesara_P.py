menuList = []
total = 0
SystemMenu = {"rice" : 10 , "soup" : 20 , "chicken" : 30 , "pork" : 35}
def showBill():
    print("----- My Food -----")
    for number in range(len(menuList)):
        print(menuList[number][0],menuList[number][1])
        #หรือใช้ totalPrice += int(priceList[number]) ก็ได้
    print("Total :", total , "THB")

while True:
    menuName = input("Please Enter Menu :")
    if(menuName.lower() == "exit"):          
        break
    else:
        menuList.append([menuName,SystemMenu[menuName]]) 
        total += int(SystemMenu[menuName])
        
showBill()