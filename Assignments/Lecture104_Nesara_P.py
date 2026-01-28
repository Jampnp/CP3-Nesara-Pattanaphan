class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Added to", self.name ,self.lastName,"'s cart")

customer1 = Customer()   
customer1.name = "John"
customer1.lastName = "Smith"
customer1.age = 35
customer1.addCart()

customer2 = Customer()   
customer2.name = "Emily"
customer2.lastName = "Rose"
customer2.age = 26
customer2.addCart()

customer3 = Customer()   
customer3.name = "Mac"
customer3.lastName = "Donald"
customer3.age = 14
customer3.addCart()