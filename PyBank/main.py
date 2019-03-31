import os
import csv

Bank_CSV = 'C:\\Users\\tswsh374\\learnpython\\Homework\\03-HW\\python-challenge\\PyBank\\Resources\\budget_data.csv'
with open(Bank_CSV, newline="") as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")
   csv_header = next(csvfile, None)
   totalNet = 0
   totalMonths = 0
   Previous = 0
   GrIncrease = 0
   GrDecrease = 0
   first = True
   for row in csvreader:
      totalNet += int(row[1])
      totalMonths += 1
      
      if first:
         First = row[1]
         first = False
      Last = row[1]
      if row != 1:
         if ((int(row[1]) - Previous) > GrIncrease):
            GrIncrease = int(row[1]) - Previous  
            
         if ((int(row[1]) - Previous) < GrDecrease):  
            GrDecrease = int(row[1]) - Previous
         Previous = int(row[1])
         
      
   AverChange = (int(Last) - int(First)) / (totalMonths - 1)
   
print("Financial Analysis")
print("----------------------")
print(f"Total Months: {str(totalMonths)}")
print(f"Total: {str(totalNet)}")
print("Average Change: $" + str("{0:.2f}".format(AverChange)))
print(f"Greatest Increase in Profits: {str(row[0])} (${str(GrIncrease)})")
print(f"Greatest Decrease in Profits: {str(row[0])} (${str(GrDecrease)})")


with open("budget_data.txt", "w") as text_file:

    print("Financial Analysis", file = text_file)
    print("----------------------------",file = text_file)
    print(f"Total Months: {str(totalMonths)}", file = text_file)
    print(f"Total: {str(totalNet)}", file = text_file)
    print("Average Change: $" + str("{0:.2f}".format(AverChange)),
    file = text_file)
    print(f"Greatest Increase in Profits: {str(row[0])} (${str(GrIncrease)})", file = text_file)
    print(f"Greatest Decrease in Profits: {str(row[0])} (${str(GrDecrease)})", file = text_file)