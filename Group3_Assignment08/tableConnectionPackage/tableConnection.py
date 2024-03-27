# Name: Group 3 (Anna Moorhead, Sonali Goyal, Cameron Hogan)
# email: moorheaa@mail.uc.edu, goyalsd@mail.uc.edu, hogancg@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date: March 28, 2024
# Course/Section: IS 4010 - 001
# Semester/Year: Spring 2024
# Brief Description of the assignment: 
# Citations:
# Anything else that's relevant:



import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
                      'Database=GroceryStoreSimulator;'
                      'uid=IS4010Login;'
                      'pwd=P@ssword2;')
cursor = conn.cursor()
cursor.execute('SELECT c.MaxQtyToPurchase, b.Brand, p.Description FROM tCouponDetail c, tBrand b, tProduct p WHERE c.ProductID=p.ProductID AND b.BrandID=p.BrandID AND p.ProductID=2')