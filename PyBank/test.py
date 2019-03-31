import os
import csv
file = 'C:\\Users\\tswsh374\\learnpython\\Homework\\03-HW\\python-challenge\\PyBank\\Resources\\budget_data.csv'
months = 0
rows = []
profitslosses = 0
with open(file, 'r') as csvfile:
   csvreader = csv.reader (csvfile, delimiter=",")
   header = next(csvreader)
   for row in csvreader:
       months = months + 1
       profitslosses = profitslosses + float(row [1])

   print(f"Total Months: {months}")
   print(f"Total: ${profitslosses}")
   print(f"Average Change: ${(profitslosses)/(months)}")
   print(f"Greatest Increase in Profits: {max(row[1])}")