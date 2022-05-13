import csv
#Setting a variable for total number of votes to 0
total_votes = 0
#Setting Candidate_options as an empty list
candidate_options = []
#defining candidate_votes as an empty dictionary
candidate_votes = {}
#declaring winning candidate variable as an emtpy string
winning_candidate = ""
#Setting a variable for winning_count to 0
winning_count = 0
#Setting a variable for winning_percentage to 0
winning_percentage = 0
#reading from csv file to print out all the rows 
with open ("Resources/election_results.csv", "r") as election_data:
    file_reader = csv.reader(election_data)
    #removing the header line from the file_reader
    headers = next(file_reader)
    #using for loop to iterate throught the rows
    for row in file_reader:
        #incrementing total_votes by 1
        total_votes = total_votes + 1
        candidate_name = row[2]
        #if condiation to find out unique candidate names and votes
        if row[2] not in candidate_options:
            candidate_name = row[2]
            candidate_options.append(row[2])
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
        #for loop to find out the vote_percentage 
for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = (votes/total_votes) * 100
   # print(f'{candidate_name} received {round(vote_percentage,1)} % of the votes')   
    if (votes > winning_count):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name
    for candidates in candidate_votes:
        winning_candidate_summary = (
        f"--------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"---------------------------\n")        
   # print(f"{candidate_name}:{vote_percentage:.1f}% ({votes:,})\n")
print(winning_candidate_summary)