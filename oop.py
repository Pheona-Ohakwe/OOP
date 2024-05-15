# Lesson 2: Assignment | OOP Fundamentals

import time

# 1. City Infrastructure Management System

# Task 1: Vehicle Registration System

class Vehicle:

    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner
    def  update_owner(self, owner):
          print ("Changing owners... ")
          self.owner= owner
          print(f"New owner is now {self.owner}. ")

vehicle_1 = Vehicle(2024,"lamborghini-urus", "Pheona")
print(vehicle_1.registration_number)
print(vehicle_1.type)
print(vehicle_1.owner)
vehicle_1.update_owner("Jacob")




# Problem Statement: Create a Python class Vehicle with attributes registration_number, type, and owner. Implement a method update_owner to change the vehicle's owner. Then, create a few instances of Vehicle and demonstrate changing the owner.


# Task 2: Event Management System Enhancement
class Event_manager:
     def __init__(self, name, time, guests):
          self.name = name
          self.time = time
          self.guests = guests

     def add_participants(self, name):
          print("Guest entering event.")
          self.guests += 1
          print(f"Welcome in {name}, so glad you could make it! Guest remaining: {self.guests}")
          
     def get_participants(self):         
          print(f"Have a nice day. Thank you for coming! Guest remaining:{self.guests} ")

guests = Event_manager ("Laura", "9:00pm", 50)
guests.add_participants("Trey")
guests.add_participants("Chinenye")
guests.get_participants()

 