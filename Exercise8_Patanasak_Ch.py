Username = input("Username : ")
Password = input("Password : ")

if Username == "Admin" and Password == "1234":
    print("Welcome to Nok-Pad-Num Store")
    print("... List of Product ...")
    print("Product 1 : Pen     price  17  baht >> press a")
    print("Product 2 : Pencil  price  10  baht >> press b")
    Product = input("Choose product : ")


    if Product == "a" or "b":
        if Product == "a":
            Product = "Pen"
            PriceProduct = 17
        else :
            Product = "Pencil"
            PriceProduct = 10
    else :
        print("Please Choose product again")
    Quantity = int(input("Quantity do you want : "))
    print()
    print("+++++++++++++++++++")
    print("Product     :", Product)
    print("Quantity    :", Quantity)
    print("Total Price :", Quantity * PriceProduct, "Baht")
    print("+++++++++++++++++++")
    print()
    print("See you Next time")
else :
    print("Login fail : Please Login Again")
