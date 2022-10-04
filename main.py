class Wallet:
    #  money = 0 The default value of money is 0
    def __init__(self, money=0):
        self.money = money

    def credit(self, amount):
        self.money = amount + self.money
        print (f"Your credit amount is {self.money}")

    def debit(self, amount):
        self.money = amount - self.money
        print (f"Your debit amount is {self.money}")
    
    def __str__(self):
        return f"{self.money}"


wallet = Wallet(15)
# wallet = Wallet(0)  # This should default money inside the wallet to 0
wallet.credit(5)
print(wallet)
wallet.debit(5)
print(wallet)



class Person:
    # Implement the code here
    def __init__(self, name, location,money):
        self.name = name
        self.location = location
        self.wallet = Wallet(money)

    def move_to(self, point):
        self.location = point 
        print (f"Your name is {self.name} and have {self.wallet} money and moved from {self.location} location to {point}")
    
    def __str__(self):
        return f"Your name is {self.name}, your location {self.location}, your money {self.wallet.money}"

person = Person("Qassem", 5, 50)
print (person.move_to(10))


class Vendor (Person):
    # implement Vendor!
    def __init__(self, name, location, money, range = 5, price = 1):
        super().__init__(name, location, money)
        self.range = range
        self.price = price
    
    def sell_to (self, customer, number_of_icecreams):
        self.location = customer.location
        self.wallet.credit(self.price * number_of_icecreams)
        customer.wallet.debit (self.price * number_of_icecreams)
        print (f"{number_of_icecreams} ice creams were sold")
        


vendor = Vendor("Abdallah",3 ,6)


class Customer (Person):
    # implement Customer!
    def __init__(self, name, location, money):
        super().__init__(name, location, money)
        
    
    def is_in_range (self,vendor):
        distance = abs(self.location - vendor.location)
        if distance <= vendor.range:
            print(f"This vendor {vendor.name} within {self.name}")
            return True
        else:
            print (f"This vendor {vendor.name} is not within {self.name}")
            return False
        
    def have_enough_money (self, vendor, number_icecreams):
        if self.wallet.money >= vendor.price * number_icecreams:
            print ("You have enough money")
            return True
            
        else:
            print ("You dont have enough money")
            return False

    def request_icecream (self, vendor, number_icecream):
        if self.is_in_range(vendor) and self.have_enough_money(vendor,number_icecream):
            Vendor.sell_to(self,number_icecream)

vendor_one = Vendor ("Talal", 3 ,60)
customer_one = Customer("Abbas", 80, 6)

customer_one._is_in_range(vendor_one)
