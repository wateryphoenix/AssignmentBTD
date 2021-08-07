systemMenu = {"ข้าวมันไก่":45,"ข้าวหมกไก่":40,"ข้าวไก่ผสม":50,"ข้าวมันไก่พิเศษ":60}
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
        menuList.append([menuName,systemMenu[menuName]])

print(menuList)
showBill()
