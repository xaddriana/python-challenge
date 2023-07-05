import os
import csv

election_data_csv = os.path.join(".", "Resources", "election_data.csv")

total_votes = 0
candidates = {}
candidate_percentages = {}
winner = ""
max_votes = 0

with open(election_data_csv, 'r') as file:
    filereader = csv.reader(file,)

    header = next(filereader)

    for row in filereader:
        total_votes += 1
        candidate = row[2]

        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

print("Election Results")
print("Total Votes:", total_votes)

for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    candidate_percentages[candidate] = round(percentage, 3)

    if votes > max_votes:
        max_votes = votes
        winner = candidate 

for candidate, percentage in candidate_percentages.items():
    vote_count = candidates[candidate]
    print(f"{candidate}: {percentage}% ({vote_count})")

print("Winner:", winner)




