menuList = []

def showBill():
    totalPrice = 0
    print("----- My Food -----")
    for number in range(len(menuList)):
       print(menuList[number][0],menuList[number][1])
       totalPrice += int(menuList[number][1])
    print("Total price : ", totalPrice)

while True:
    menuName = input("Please Enter Manu : ")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price : ")
        menuList.append([menuName,menuPrice])

print(menuList)
showBill()
