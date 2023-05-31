#Team 8
#Kyle Parkinson, Landon Webb, Joseph Christensen, Alexandra Mitchell, Braden Allfrey, Jenessa Finch
#This program tracks 100 orders of customers that enter your hamburger restaurant and displays the total hamburgers each customer eats next to their name
 
#Importing random allows the program to use the random function to generate a customer name. 	
import random


#Order Class
class Order:
   def __init__(self):
	#instance variable connected to the method that will generate random orders.
       self.burger_count = self.randomBurgers()


#Method to generate random number of burgers ordered.
   def randomBurgers(self):
       return random.randint(1, 20)


#Person Class
class Person:
   def __init__(self):
	#instance variable created from the random name method.
       self.customer_name = self.randomName()


#Method to generate a random name (customer)
   def randomName(self):
       customers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
       return random.choice(customers) #This random function will take a random name from the list of customers.




#Customer Class
class Customer(Person):
   def __init__(self):
	#Here we are calling the super or parent function of 'Person'. The object 'Customer' will first run the constructor from the parent and then run its own
       super().__init__() 
       self.order = Order()


customerQueue = [] #This is setting this variable as a list
customerDict = {} #This is setting this variable as a dictionary


iCustomer = 100 #variable used for the range in the loop function

#for loop that will create the customer instance objects, add them to the dictionary list
for iCount in range (0, iCustomer):
   customer = Customer()
   customerQueue.append(customer)
   customerQueue.pop(0) #This pop function removes the first customer after they have moved through the queue
   if customer.customer_name in customerDict:
       customerDict[customer.customer_name] += customer.order.burger_count
   else:
       customerDict[customer.customer_name] = customer.order.burger_count


  

#This creates a lambda function in order to sort the customers from the greatest number of burgers purchased to the fewest. 
listSortedCustomers = sorted(customerDict.items(), key=lambda x: x[1], reverse=True)



for customer in listSortedCustomers:
   print(customer[0].ljust(19), customer[1])


