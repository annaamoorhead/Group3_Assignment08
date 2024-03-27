# Name: Group 3 (Anna Moorhead, Sonali Goyal, Cameron Hogan)
# email: moorheaa@mail.uc.edu, goyalsd@mail.uc.edu, hogancg@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date: March 28, 2024
# Course/Section: IS 4010 - 001
# Semester/Year: Spring 2024
# Brief Description of the assignment: connecting a database to Eclipse and joining tables in Eclipse too 
# Citations:
# Anything else that's relevant: yes there are 3 different coupon for the same product so it populated all 3 coupon into sentences

from tableConnectionPackage.tableConnection import *

if __name__ == "__main__":
    for row in cursor:
        BrandID = row[1] 
        ProductID= row[0]
        MaxQtyToPurchase= row[2]
        print("The maximum quantity that I am able to purchase of the product " + str(ProductID) + " by the brand " + str(BrandID)+ " is " + str(MaxQtyToPurchase))
