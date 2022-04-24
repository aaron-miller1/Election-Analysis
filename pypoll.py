import csv

import os


#  Assign a variable to load a file from a path

file_to_load = os.path.join('Election-Analysis', 'Resources', 'election_results.csv')

# assign a variable to save the file to a path

file_to_save = os.path.join('Election-Analysis', 'election_analysis.txt')

# Initialize total votes

total_votes = 0

# cand options

candidate_options = []

# declare candidate vote dict

candidate_votes = {}

# winning cand and winning count ticker

winning_candidate = ""

winning_count = 0

winning_percentage = 0


# open the lection results and read

with open(file_to_load) as election_data:
   
   # To DO: read and analyze
   file_reader = csv.reader(election_data)

# Read and print the header row
   headers = next(file_reader)

   for row in file_reader:
      
      # add to vote count

      total_votes += 1

# Print candidate name from each row

      candidate_name = row[2]

      if candidate_name not in candidate_options:

         candidate_options.append(candidate_name)

         # tracking candidates votes

         candidate_votes[candidate_name] = 0

      # add a vote to that candidate count

      candidate_votes[candidate_name] += 1

     
# Iterate through the candidate list
    
for candidate_name in candidate_votes:

   # Retrieve vote count of a candidate

   votes = candidate_votes[candidate_name]

   # calculate the % of the votes

   vote_percentage = float(votes) / float(total_votes) * 100


   # To Do: print out each cand name, count, and %

   print(f'{candidate_name}: {vote_percentage: .1f}% ({votes:,})\n')


   if (votes > winning_count) and (vote_percentage > winning_percentage):

      # If true then set winning_count = votes and winng % = vote %

      winning_count = votes

      winning_percentage = vote_percentage

      # set winning cand = to cand name

      winning_candidate = candidate_name

winning_candidate_summary = (
   f"-------------------------\n"

   f"Winner: {winning_candidate}\n"

   f"Winning Vote Count: {winning_count}\n"

   f"Winning Percentage: {winning_percentage: .1f}%\n"

   f"-------------------------\n")

print(winning_candidate_summary)