In this task, we will build a system for buying and selling ice-cream.

## Setup
1. Fork [this repo](https://github.com/JoinCODED/TASK-Python-Classes).
2. Clone it in your Development/Foundations directory.
3. Write the code in `main.py`.
4. Push your code when you're done.

## Wallet Class

This class `Wallet` keeps track of money. It has the following properties and methods:

1. `money`: The amount of money in the wallet. Defaults to 0.
2. `credit(amount)`: this method adds the `amount` to the `money` property, then prints the new value of `money` in a nice message.
3. `debit(amount)`:this method subtracts the `amount` from the `money` property, then prints the new value of `money` in a nice message.

## Person Class

This class `Person` defines a person with a name, location and wallet. It has the following properties and methods:

1. `name`: name of said person
2. `location`: a number that represents the person's place (Any number, don't overthink it).
3. `wallet`: a `Wallet` **instance**. Create a Wallet instance and pass it as a property to this class.
4. `moveTo(point)`: updates the `location` property to `point`, then prints the new value of `location` in a nice message.

## Vendor Class

This class `Vendor` is a subclass of `Person`. Yes, you need to inherit! It has the following properties and methods:

1. `range`: the maximum distance this vendor can travel - initially 5
2. `price`: the cost of a single ice cream - initially 1
3. `sellTo(customer, number_of_icecreams):` sells a specific number of ice creams to the customer by doing the following:
   - Moves to the customer's location
   - Transfers money from the customer's wallet to the vendor's wallet
   - Prints a nice message saying how many icecreams were sold

## Customer Class

This class `Customer` is a subclass of `Person`. Yes, you need to inherit! It has the following properties and methods:

1. `_is_in_range(vendor)`:
   - Checks if the customer is in range of vendor.
   - To check the range, you need to find the distance between the vendor and customer by subtracting their locations from each other (Convert it to a positive number).
   - If the distance is less than or equal to the vendor's range, then this customer is within range.
   - Prints a message saying that the customer is in range or not
2. `_have_enough_money(vendor, number_of_icecreams):`
   - Checks if the customer has enough money to buy a specific number of ice creams from vendor.
   - Prints a message saying if the customer has enough money or not.
3. `request_icecream(vendor, number_of_icecreams):`
   - If the customer is in the vendor's range and has enough money for ice cream, a request is sent to the vendor.
   - Print a message saying that a request has been made.
