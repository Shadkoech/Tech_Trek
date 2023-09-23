#!/usr/bin/python3


class Customer:
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type

    def update_membership(self, new_membership):
        print("Upgrading/downgrading membership")
        self.membership_type = new_membership

    def __str__(self):
        print("converting to string")
        return self.name + " " + self.membership_type

    def print_all_customers(Customers):
        for customer in customers:
            print(customer)

customers = [Customer("Carson", "Gold"), 
          Customer("Anne", "Bronze")]

Customer.print_all_customers(customers)

# print(Customers[1])
# Customers[1].update_membership("Gold")
# print(Customers[1])
# print(Customers[0])
