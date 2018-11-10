#import dependencies
import os
import csv
#read csv
csvpath = os.path.join('..', 'PyPoll', 'Resources', 'election_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    csv_header = next(csvreader)
#assign values
    vid = 12864552
    total_votes = 0
    candidates = []
    khan_vote = 0
    correy_vote = 0
    li_vote = 0
    o_tooley_vote = 0
#The total number of votes cast
    for row in csvreader:
        if vid != row[0]:
            total_votes = total_votes + 1
#print(total_votes)
#A complete list of candidates who received votes
        vote = row[2]
        if vote not in candidates: 
            candidates.append(row[2])
#print(candidates)
#The total number of votes each candidate won
        if row[2] == "Khan":
            khan_vote = khan_vote + 1
        elif row[2] == "Correy":
            correy_vote = correy_vote + 1
        elif row[2] == "Li":
            li_vote = li_vote + 1
        elif row[2] == "O'Tooley":
            o_tooley_vote = o_tooley_vote + 1
#print(khan_vote, correy_vote, li_vote, o_tooley_vote)
#The percentage of votes each candidate won
        percent_khan = khan_vote/total_votes * 100
        percent_correy = correy_vote/total_votes * 100
        percent_li = li_vote/total_votes * 100
        percent_o_tooley = o_tooley_vote/total_votes * 100
#print(percent_khan, percent_correy, percent_li, percent_o_tooley)
#The winner of the election based on popular vote
        winner_percent = max(percent_khan, percent_correy, percent_li, percent_o_tooley)
#print(winner_percent)
#we can see that the winner is khan

#print values found
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"Khan: {percent_khan}% ({khan_vote})")
print(f"Correy: {percent_correy}% ({correy_vote})")
print(f"Li: {percent_li}% ({li_vote})")
print(f"O'Tooley: {percent_o_tooley}% ({o_tooley_vote})")
print("-------------------------")
print(f"Winner: Khan")
print("-------------------------")

#export text as txt
def outputfile():
    outputname = 'election_results.txt'
    myfile = open(outputname, 'w')
    myfile.write('Election Results')
    myfile.write('\n----------------------------')
    myfile.write(f'\nTotal Votes: {total_votes}')
    myfile.write('\n----------------------------')
    myfile.write(f'\nKhan: {percent_khan}% ({khan_vote})')
    myfile.write(f'\nCorrey: {percent_correy}% ({correy_vote})')
    myfile.write(f'\nLi: {percent_li}% ({li_vote})')
    myfile.write(f"\nO'Tooley: {percent_o_tooley}% ({o_tooley_vote})")
    myfile.write('\n----------------------------')
    myfile.write(f'\nWinner: Khan')
    myfile.write('\n----------------------------')
    myfile.close()
outputfile()
