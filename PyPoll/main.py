# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("PyPoll", "Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("PyPoll", "analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidates = []
candidate_vote_percentage = []
total_vote_candidates = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data, delimiter =",")


    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes = total_votes + 1


        # Get the candidate's name from the row
        candidate_name = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidates:
            candidates.append(candidate_name) #add candidates name

        # Add a vote to the candidate's count
            total_vote_candidates[candidate_name] = 0
        
        total_vote_candidates[candidate_name] = total_vote_candidates[candidate_name] + 1

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:}\n"
        f"-------------------------\n")
    
    print(election_results, end="")

    # Write the total vote count to the text file
    txt_file.write(election_results)

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate_name in total_vote_candidates:

        # Get the vote count and calculate the percentage
        votes = total_vote_candidates[candidate_name]
        candidate_vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = f"{candidate_name} : {candidate_vote_percentage:.3f}% ({votes:})\n"

       


        # Update the winning candidate if this one has more votes
        if (votes > winning_count) and (candidate_vote_percentage > winning_percentage):
             winning_count = votes
             winning_candidate = candidate_name
             winning_percentage = candidate_vote_percentage

        # Print and save each candidate's vote count and percentage
        print(candidate_results)

        txt_file.write(candidate_results)


    # Generate and print the winning candidate summary
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n"
    )
    print(winning_candidate_summary)

    # Save the winning candidate summary to the text file
    txt_file.write(winning_candidate_summary)
