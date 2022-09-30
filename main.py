class Wallet:
    def __init__(self, money):
        self.money = money

    def credit(self, amount):
        self.money = amount + self.money
        print (f"Your credit amount is {self.money}")

    def debit(self, amount):
        self.money = amount - self.money
        print (f"Your debit amount is {self.money}")


wallet = Wallet(6)
# wallet = Wallet(0)  # This should default money inside the wallet to 0
wallet.credit(5)
print(wallet.money)



class Person:
    # Implement the code here
    def __init__(self, name, location,money):
        self.name = name
        self.location = location
        self.money = Wallet(money)

    def move_to(self, point):
        self.location == point 
        print (f"Your name is {self.name} and have {self.money} money and moved from {self.location} location to {point}")

person = Person("Qassem", 5, 50)
print (person.move_to(10))


class Vendor (Person):
    # implement Vendor!
    def __init__(self, name, location, money, range, price):
        super().__init__(name, location, money)
        self.range = range.max (5)
        self.price = price + 1
    
    def sell_to (self, customer, number_of_icecreams):
        self.customer = customer
        self.number_of_icecreams = number_of_icecreams
        self.move_to(customer,location)
        self.money.credit(self.price * number_of_icecreams)
        


# vendor = Vendor("Abdallah", 3, 6)


class Customer:
    # implement Customer!
    pass


# customer = Customer("Abdallah", 3, 6)
