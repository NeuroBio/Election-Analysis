import csv
import os

# get data and create file for analysis
input_path = os.path.join('Resources', 'election_results.csv')
output_path = os.path.join('analysis', 'election_analysis.txt')
# analysis = open(output_path, "w")

# Load in data
with open(input_path) as election_file:
    election_data = csv.reader(election_file)
    next(election_data)

    num_votes = 0

    for row in election_data:

        # Get the number of votes cast from the length of the data.
        num_votes += 1

        # analysis.write()
    # Get a set of the candidates
    # Create a data structure to hold the votes per candidate
    # Use a for loop to tally each vote towards the apporpriate candidate
    # Get the precentage of the vote by dividing votes/candidate by number of votes cast.
        #analysis.write()
    # Use a one-time-pass method to get the candidate with the largest precentage
        #analysis.write()

# analysis.close()
