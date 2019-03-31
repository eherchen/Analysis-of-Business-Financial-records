import os
import csv

Election_CSV ='C:\\Users\\tswsh374\\learnpython\\Homework\\03-HW\\python-challenge\\PyPoll\\Resources\\election_data.csv'

with open(Election_CSV, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')  
    #print(csvreader)
    csv_header = next(csvreader)
    #election_header = next(electionfile, None)
    #print(f"CSV Header: {csv_header}")
              
    total_votes = 0
    rows = []
    Khan_Votes = 0
    Correy_Votes = 0 
    Li_Votes = 0
    OTooley_Votes = 0
for row in open(Election_CSV):
    total_votes = total_votes + 1
    if row[2] == "Khan":
        Khan_Votes = Khan_Votes + 1
    elif (row[2] == "Correy"):
        Correy_Votes = Correy_Votes + 1
    elif (row[2] == "Li"):
        Li_Votes = Li_Votes + 1
    elif (row[2] == "O'Tooley"):
        OTooley_Votes = OTooley_Votes + 1
    
    Khan_Percentage = round(100 * Khan_Votes/total_votes, 3)
    Correy_Percentage = round(100 * Correy_Votes/total_votes, 3)
    Li_Percentage = round(100 * Li_Votes/total_votes, 3)
    OTooley_Percentage = round(100 * OTooley_Votes/total_votes, 3)

    candidates = {'Khan': Khan_Percentage, 'Correy': Correy_Percentage, 'Li': Li_Percentage, 'OTooley': OTooley_Percentage}
    winner = max(candidates, key=candidates.get)
    
print("Election Results")
print("-------------------------")
print("Total Votes: "+ str(total_votes))
print("-------------------------")
print("Khan: " +  str(Khan_Percentage) +"%  (" + str(Khan_Votes)+ ")")
print("Correy: " +  str(Correy_Percentage) +"%  (" + str(Correy_Votes)+ ")")
print("Li: " +  str(Li_Percentage) + "%  (" + str(Li_Votes)+ ")")
print("OTooley: " +  str(OTooley_Percentage) +"%  (" + str(OTooley_Votes)+ ")")
print("-------------------------")
print("Winner: " + winner)
print("-------------------------")
with open("election_data.txt", "w") as text_file:
    print("Election Results", file = text_file)
    print("-------------------------", file = text_file)
    print("Total Votes: "+ str(total_votes), file = text_file)
    print("-------------------------", file = text_file)
    print("Khan: " +  str(Khan_Percentage) +"%  (" + str(Khan_Votes)+ ")", file = text_file)
    print("Correy: " +  str(Correy_Percentage) +"%  (" + str(Correy_Votes)+ ")", file = text_file)
    print("Li: " +  str(Li_Percentage) + "%  (" + str(Li_Votes)+ ")", file = text_file)
    print("OTooley: " +  str(OTooley_Percentage) +"%  (" + str(Khan_Votes)+ ")", file = text_file)
    print("-------------------------", file = text_file)
    print("Winner: " + winner, file = text_file)
    print("-------------------------", file = text_file)