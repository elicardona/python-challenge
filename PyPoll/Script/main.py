import os
import csv

csvpath = os.path.join("..", "Resources", "election_data.csv")

total_votes = 0

candidates = {}

 

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header=next(csvreader)

    for row in csvreader:
            total_votes = total_votes + 1

            if row[2] in candidates:
                candidates[row[2]] = candidates[row[2]] + 1
            else:
                candidates[row[2]] = 1
    print("Election Results")
    print("______________________")
    print(f"Total Votes: {total_votes}")
    print("______________________")





    for key, value in candidates.items():
        percent_votes = (value/3521001)* 100     
        candidate_list= (f"{key}:{percent_votes}  ({value})")
        print(f"{key}:{percent_votes}  ({value})")
    print("______________________")
    winner = max(candidates, key = candidates.get)
    print(f"Winner: {winner}")      

    with open("output.txt","w") as txt_file:
        txt_file.write("Election Results\n")
        txt_file.write("______________________\n")
        txt_file.write(f"Total Votes: {total_votes}\n")
        txt_file.write("___________________________\n")
        txt_file.write(f"{candidate_list}\n")
        txt_file.write("______________________\n")
        txt_file.write(f"Winner: {winner}\n")   


