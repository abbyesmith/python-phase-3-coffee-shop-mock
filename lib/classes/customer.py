# from classes.order import Order

class Customer:
    def __init__(self, name):
        self.name =name

    def get_name(self):
        return self._name
    def set_name(self, name):
        if (type(name) is str):
            if 1<= len(name) <= 15:
                self._name = name
    name = property(get_name, set_name)

    def orders(self):
        from .order import Order
        customer_list = []
        for order in Order.all:
            if order.customer == self:
                customer_list.append(order)
        return customer_list
    
    def coffees(self):
        from .order import Order
        type_coffees = []
        for order in Order.all:
            if order.coffee not in type_coffees:
                if order.customer == self:
                    type_coffees.append(order.coffee)
        return type_coffees
    
    def create_order(self, coffee, price=0):
        from .order import Order
        return Order(self, coffee, price)


        





#### Customer

# - `Customer __init__(self, name)`
#   - Customer should be initialized with a name
# - `Customer property name`
#   - Return name
#   - Names must be of type `str`
#   - Names must be between 1 and 15 characters, inclusive
#   - if you are using exceptions comment out the test on lines 32 - 35 in the customer_test.py and uncomment lines 37 - 45

# - `Customer orders()`
#   - Returns a list of all orders a customer has ordered
#   - orders must be of type `Order`
# - `Customer coffees()`
#   - Returns a **unique** list of all coffees a customer has ordered
#   - Coffees must be of type `Coffee`

# - `Customer create_order(coffee, price)`
#   - given a **coffee object** and a price(as an integer), creates a
#     new order and associates it with that customer and coffee.