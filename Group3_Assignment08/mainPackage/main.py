# Name: Group 3 (Anna Moorhead, Sonali Goyal, Cameron Hogan)
# email: moorheaa@mail.uc.edu, goyalsd@mail.uc.edu, hogancg@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date: March 28, 2024
# Course/Section: IS 4010 - 001
# Semester/Year: Spring 2024
# Brief Description of the assignment: 
# Citations:
# Anything else that's relevant:

from tableConnectionPackage.tableConnection import *
from functionPackage.function import *

for row in cursor:
    print(row)
    
print("The maximum quantity that I am able to purchase of the product" + str(row.ProductID) + "by the brand" + str(row.BrandID)+ "is" + str(row.MaxQtyToPurchase))


