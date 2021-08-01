def login():
    usernameInput = input("Username = ")
    passwordInput = input("Password = ")
    if usernameInput == "admin" and passwordInput == "1234":
        return True
    else:
        return False

def showManu():
    print("Nok - Ped - Num Shop")
    print("1. Vat Calculator")
    print("2. Price Calculator")
def manuSelecte():
    userSelected = int(input(">>"))
    return userSelected
def vatCalculate(totalprice):
    vat = 7
    result = totalprice + (totalprice * vat / 100)
    return result
def priceCalculate():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculate(price1 + price2)

if login() == True :
    showManu()
    manuSelecte = manuSelecte()
    if manuSelecte == 1:
        totalprice = int(input("Price (THB) : "))
        print(vatCalculate(totalprice))
    elif manuSelecte == 2:
        print(priceCalculate())
else :
    print("Login Again")
