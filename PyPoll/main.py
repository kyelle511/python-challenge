import os
import csv

#path to collect the data
poll_csv=os.path.join("Resources","election_data.csv")

with open(poll_csv,'r') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    header=next(csvreader)

    total_votes=0
    candidate_options=[]
    candidate_votes={}
    candidate_name=0
    
    for row in csvreader:
        id=str(row[0])
        county=str(row[1])
        candidate_name=str(row[2])

#count the total number of votes
        total_votes+=1

#create the list of candidates (https://stackoverflow.com/questions/24441606/how-to-create-a-list-in-python-with-the-unique-values-of-a-csv-file
#And thanks to LAs Peter Osipchuk & Jonathan Leverenz for helping me modify this so it created a vote count while looping through)
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            
            candidate_votes[candidate_name]=0
        
        candidate_votes[candidate_name]+=1
       
    print(f'Election Results')
    print(f'----------------------------------------')
    print(f'Total Votes: {str(total_votes)}')
    print(f'----------------------------------------')

#print candidate votes and percentages (Thanks to Jonathan Leverenz for helping me find a clearer way to code this)
    for candidate in candidate_votes:
        votes=candidate_votes[candidate]
        percentage_votes=round((votes/total_votes)*100,3)
        voter_output=f"{candidate}: {percentage_votes}% ({votes})\n"
        print(voter_output, end="")

 #find the winner (https://www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-80.php#:~:text=Use%20max()%20with%20the,value%20in%20the%20given%20dictionary)      
    winner=max(candidate_votes, key=candidate_votes.get)
    
    print(f'----------------------------------------')
    print(f'Winner: {str(winner)}')
    print(f'----------------------------------------')

#create txt file with results (https://www.pythontutorial.net/python-basics/python-create-text-file/)
with open('analysis/analysis.txt','w') as f:
    print(f'Election Results', file=f)
    print(f'----------------------------------------', file=f)
    print(f'Total Votes: {str(total_votes)}', file=f)
    print(f'----------------------------------------', file=f)

    for candidate in candidate_votes:
        votes=candidate_votes[candidate]
        percentage_votes=round((votes/total_votes)*100,3)
        voter_output=f"{candidate}: {percentage_votes}% ({votes})\n"
        print(voter_output, end="", file=f)

    winner=max(candidate_votes, key=candidate_votes.get)
    
    print(f'----------------------------------------', file=f)
    print(f'Winner: {str(winner)}', file=f)
    print(f'----------------------------------------',file=f)
    f.close()
        




 
    

