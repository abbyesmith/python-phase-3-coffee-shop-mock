# from classes.order import Order

class Coffee:
    def __init__(self, name):
        if type(name) is str:
            self._name = name
    
    def get_name(self):
        return self._name
    def set_name(self, new_name):
        print("Cannot change coffee name")
    name = property(get_name, set_name)
    
    def orders(self):
        from .order import Order
        order_list = []
        for order in Order.all:
            if order.coffee == self:
                order_list.append(order)
        return order_list

    def customers(self):
        from .order import Order
        customer_list = []
        for order in Order.all:
            if order.coffee == self:
                customer_list.append(order.customer)
        return list(set(customer_list))

    def num_orders(self):
        from .order import Order
        count = 0
        for order in Order.all:
            if order.coffee == self:
                count += 1
        return count

    def average_price(self):
        orders_prices = [order.price for order in self.orders()]
        sum_price = sum(orders_prices)
        return sum_price/self.num_orders()
# No idea how to test this or if it is even close
    # def average_price(self, num_orders):
        # from .order import Order
        # sum = 0
        # for order in Order.all:
        #     if order.coffee == self:
        #         sum += order.price
        # return sum/num_orders()

    
#### Coffee

# - `Coffee __init__(self, name)`
#   - Coffees should be initialized with a name, as a string
# - `Coffee property name`
#   - Returns the coffee's name
#   - Should not be able to change after the coffee is created
#   - hint: hasattr()
#   - if you are using exceptions comment out the test on lines 20 - 24 in the coffee_test.py and uncomment lines 26 - 30

#### Coffee

# - `Coffee orders()`
#   - Returns a list of all orders for that coffee
#   - orders must be of type `Order`
# - `Coffee customers()`
#   - Returns a **unique** list of all customers who have ordered a particular coffee.
#   - Customers must be of type `Customer`

#### Coffee

# - `Coffee num_orders()`
#   - Returns the total number of times that coffee has been ordered
# - `Coffee average_price()`
#   - Returns the average price for a coffee based on its orders
#   - Reminder: you can calculate the average by adding up all the orders prices and
#     dividing by the number of orders