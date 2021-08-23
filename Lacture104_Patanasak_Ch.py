class Customer:       
    name = ""
    lastName = ""
    age = 0

    def addCart(self):        
        print("Added to",self.name,self.lastName,"'s Cart")

customer1 = Customer()         
customer1.name = "Patanasak"
customer1.lastName = "Chunkhajorn"
customer1.age = "31"                   
customer1.addCart()            

customer2 = Customer()
customer2.name = "Pikachu"
customer2.lastName = "Masara"
customer2.age = "25"
customer2.addCart()

customer3 = Customer()
customer3.name = "Nobita"
customer3.lastName = "Nobi"
customer3.age = "14"
customer3.addCart()
