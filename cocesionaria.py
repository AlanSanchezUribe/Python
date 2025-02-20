class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.available = True
    
    def buy(self):
        if not self.available:
            self.available = True
            print (f"The Vehicle {self.brand} {self.model} has been bought")

    def sell(self):
        if self.available:
            self.available = False
            print (f"The Vehicle {self.brand} {self.model} has been sold")

class Customer:
    def __init__ (self, name, customer_id):
        self.name = name
        self.customer_id = customer_id
        self.vehicles_bought = []

    def buy_vehicle(self, vehicle):
        if vehicle.available:
            vehicle.sell()
            self.vehicles_bought.append(vehicle)
        else:
            print (f"The Vehicle {vehicle.brand} {vehicle.model} is not available")

    def sell_vehicle(self, vehicle):
        if vehicle in self.vehicles_bought:
            vehicle.buy()
            self.vehicles_bought.remove(vehicle)
        else:
            print (f"The Vehicle {vehicle.brand} {vehicle.model} is not owned by the customer")

class Dealership:
    def __init__ (self, name):
        self.name = name
        self.vehicles = []
        self.customers = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print (f"The Vehicle {vehicle.brand} {vehicle.model} has been added to the dealership")

    def add_customer(self, customer):
        self.customers.append(customer)
        print (f"The Customer {customer.name} has been added to the dealership")

    def display_vehicles(self):
        print("Vehicles in the dealership are:")
        for vehicle in self.vehicles:
            if vehicle.available:
                print (f"{vehicle.brand} {vehicle.model} {vehicle.year}")

    def display_customers(self):
        print("Customers in the dealership are:")
        for customer in self.customers:
            print (f"{customer.name} with ID {customer.customer_id}")


#create vehicles
vehicle1 = Vehicle("Toyota", "Corolla", 2019)   
vehicle2 = Vehicle("Honda", "Civic", 2018)
vehicle3 = Vehicle("Ford", "Fiesta", 2017)

#create customers
customer1 = Customer("John", 1)
customer2 = Customer("Alice", 2)

#create dealership
dealership = Dealership("Car Dealership")

#add vehicles to dealership
dealership.add_vehicle(vehicle1)
dealership.add_vehicle(vehicle2)
dealership.add_vehicle(vehicle3)

#add customers to dealership
dealership.add_customer(customer1)
dealership.add_customer(customer2)

#display vehicles
dealership.display_vehicles()

#display customers
dealership.display_customers()

#customer buys a vehicle
customer1.buy_vehicle(vehicle1)

#display vehicles
dealership.display_vehicles()

#customer sells a vehicle
customer1.sell_vehicle(vehicle1)

#display vehicles
dealership.display_vehicles()

    