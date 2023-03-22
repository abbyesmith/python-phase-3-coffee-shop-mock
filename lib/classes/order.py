from .coffee import Coffee
from .customer import Customer

class Order:
    all = []

    def __init__(self, customer, coffee, price=0):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)
    
    def get_coffee(self):
        return self._coffee
    def set_coffee(self, input):
        if type(input) == Coffee:
            self._coffee = input
        else:
            print("Not a valid coffee")
    coffee = property(get_coffee, set_coffee)

    def get_customer(self):
        return self._customer
    def set_customer(self, input):
        if type(input) == Customer:
            self._customer = input
        else:
            print("Not a valid customer")
    customer = property(get_customer, set_customer)

    def get_price(self):
        return self._price
    def set_price(self, price):
        if (type(price) is int) or (type(price) is float):
            if 1<=len(str(price))<=10:
                self._price = price
        else:
            return("Price must be a number between 1 and 10 digits")
    price = property(get_price, set_price)



#### Order

# - `Order __init__(self, customer, coffee, price)`
#   - Orders should be initialized with a customer, coffee, and a price (a number)
# - `Order property price`
#   - Returns the price for a coffee
#   - Price must be a number between 1 and 10, inclusive



#### Order

# - `Order property customer`
#   - Returns the customer object for that order
#   - Must be of type `Customer`
# - `Order property coffee`
#   - Returns the coffee object for that order
#   - Must be of type `Coffee`
