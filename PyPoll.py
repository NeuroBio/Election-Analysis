import csv
import os

# create file for analysis
output_path = os.path.join('analysis', 'election_analysis.txt')
open(output_path, "w")

# Load in data
input_path = os.path.join('Resources', 'election_results.csv')
with open(input_path) as election_data:
    print(election_data)

    # Get the number of votes cast from the length of the data. (print?)
    # Get a set of the candidates
    # Create a data structure to hold the votes per candidate
    # Use a for loop to tally each vote towards the apporpriate candidate
    # Get the precentage of the vote by dividing votes/candidate by number of votes cast. (print candidate + raw vote tally + precentage?)
    # Use a one-time-pass method to get the candidate with the largest precentage (print winner?)

# close(output_path)