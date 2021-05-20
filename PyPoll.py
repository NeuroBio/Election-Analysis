import csv
import os

# get data and create file for analysis
input_path = os.path.join('Resources', 'election_results.csv')
output_path = os.path.join('analysis', 'election_analysis.txt')

#set variables
candidate_options = []
candidate_votes = {}
num_votes = 0

# Load in data
with open(input_path) as election_file:
    election_data = csv.reader(election_file)
    next(election_data)


    for row in election_data:

        # Get the number of votes cast from the length of the data.
        num_votes += 1

        # Get a set of the candidates
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0

        # Tally each vote towards the apporpriate candidate
        candidate_votes[candidate_name] += 1 

    # Create a data structure to hold the votes per candidate
    # Use a for loop to tally each vote towards the apporpriate candidate
    # Get the precentage of the vote by dividing votes/candidate by number of votes cast.
    # Use a one-time-pass method to get the candidate with the largest precentage
# Write results to file
# analysis = open(output_path, "w")
for candidate in candidate_options:
    vote_percentage = (candidate_votes[candidate] / num_votes) * 100
    print(f'{candidate} recieved {vote_percentage:.1f}% of the vote.')
# analysis.write()
# analysis.close()
