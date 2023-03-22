#!/usr/bin/env python3
# import ipdb

from classes.customer import Customer
from classes.order import Order
from classes.coffee import Coffee

# Customers
abby = Customer("Abby")
mike = Customer("Mike")
print(abby.name)

# Coffees
latte = Coffee("Latte")
espresso = Coffee("espresso")
print(latte.name)

# Orders
o1 = Order(abby, espresso, 5)
o2 = Order(mike, espresso, 5)
o3 = Order(abby, latte, 6)
print(o1.customer.name)
print(latte.average_price())
# if __name__ == '__main__':
#     print("HELLO! :) let's debug")

#     ipdb.set_trace()
