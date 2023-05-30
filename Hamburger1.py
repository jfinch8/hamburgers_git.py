import random


#Order Class
class Order:
    def __init__(self):
        self.burger_count = self.randomBurgers()


    def randomBurgers(self):
        return random.randint(1, 20)


#Person Class
class Person:
    def __init__(self):
        self.customer_name = self.randomName()


    def randomName(self):
        customers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
        return random.choice(customers)


#Customer Class
class Customer(Person):
    def __init__(self):
        super().__init__()
        self.order = Order()

customerQueue = []
customerDict = {}

iCustomer = 100

for iCount in range (0, iCustomer):
    customer = Customer()
    customerQueue.append(customer)
    customerQueue.pop(0)
    if customer.customer_name in customerDict:
        customerDict[customer.customer_name] += customer.order.burger_count
    else:
        customerDict[customer.customer_name] = customer.order.burger_count

    

listSortedCustomers = sorted(customerDict.items(), key=lambda x: x[1], reverse=True)


for customer in listSortedCustomers:
    print(customer[0].ljust(19), customer[1])


