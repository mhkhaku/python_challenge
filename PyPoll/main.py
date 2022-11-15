# Creating a Python Scrip in helping a small, rural town modernize its vote-counting process.
# Below script analyzes the votes and calculates each of the following values:
    # The total number of votes cast
    # A complete list of candidates who received votes
    # The percentage of votes each candidate won
    # The total number of votes each candidate won
    # The winner of the election based on popular



import os
import csv

# Importing CSV file to Python

election_csv = os.path.join('Resources', 'election_data.csv')


with open(election_csv, 'r') as file_handler:
    
    csv_reader = csv.reader(file_handler, delimiter = ',')
    csv_header = next(file_handler)

    
#Calculating Total # of votes cast

    vote_data = list(csv_reader)
    total_vote = len(vote_data)

    print("Election Results")
    print("--------------------------------------")

    print(f"The total number of votes is {total_vote}")
    print("--------------------------------------")

# Calculating total # of votes per candidate. 
 
    candidates = []
    for row in vote_data:
        if row[2] not in candidates:
            candidates.append(row[2])
    
    votes = {}
    for name in candidates:
        votes[name]=0
    
    for name in candidates:
        for row in vote_data:
            if row[2]==name:
                votes[name]=votes[name]+1

    percentage_votes={}
    for name in votes:
        percentage_votes[name]= votes[name]/total_vote*100


    for x in votes:
        print(x + ":   " +str(round(percentage_votes[x],2)) + "%  "+ "("+str(votes[x])+")")


# Calculating winner   


    winner = ""
    max_vote=0
    for name in votes:
        if votes[name]>max_vote:
            winner=name
            max_vote=votes[name]
    
    print("--------------------------------------")
    print("Winner: " +winner)
    print("--------------------------------------")

    # Exporting data to a text file

    electionfile = open("electiondata.txt","w")
    electionfile.write("Elections Results\n")
    electionfile.writelines("--------------------------------------\n")
    electionfile.writelines("The total number of votes is "+ str(total_vote))
    electionfile.write(" \n")
    electionfile.writelines("--------------------------------------")
    electionfile.write(" \n")

for x in votes:
        electionfile.writelines([x + ":   " +str(round(percentage_votes[x],2)) + "%  "+ "("+str(votes[x])+")\n"])     

electionfile.writelines("--------------------------------------\n")
electionfile.writelines("Winner:  " + (winner))    
electionfile.write(" \n")
electionfile.writelines("--------------------------------------\n")
electionfile.close() 

 


    

    


