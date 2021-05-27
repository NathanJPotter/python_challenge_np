# This is a script to run an analysis of election_data for the PyPoll exercise

# Import the os module for creating file paths across operating systems. And import the module for reading CSV files

import os
import csv

# Specify os path for reading csv file

csv_path = os.path.join('..', 'PyPoll/Resources', 'election_data.csv')

# Specify os path for writing text file

text_path = os.path.join('..', 'PyPoll/Analysis', 'election_results.txt')

# Create empty dictionaries to hold data

votes = []

# Create an empty dictionary to store candidate vote count

vote_count = {}

# Create an empty dictionary to store candidate vote percentage

vote_percentage = {}

# Create a variable to hold the total vote count

winner_count = 0

# Open and read CSV file

with open(csv_path, newline="") as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")

    # Skip the header row
    next(csvreader)

    # Loop through csv file

    for row in csvreader:

        # Add voting choices to votes list
        votes.append(row[2])

        # Number of votes for each candidate
        if row[2] in vote_count:
            vote_count[row[2]] += 1

        # If candidate does not exist in the dictionary add them and set value as 1
        else:
            vote_count[row[2]] = 1


# Get the total number of votes cast

total_votes = (len(votes))

# Retrieve the full list of candidates who received votes


# Calculate the percentage of votes each candidate won



# Calculate the number of votes each candidate won



# Retrieve the winer of the election based on number of votes



# Give text file the title 'Election Results'. Print.

print("Election Results")
print("------------------------------")
print("Total Votes: " + str(total_votes))
print("------------------------------")

# Write title to text file

text_file_title = ["Election Results \n", "------------------------------ \n"]

with open(text_path, 'w') as f:
    f.writelines(text_file_title)
    f.write('\n')
    f.write("Total Votes: " + str(total_votes))
    f.write('\n')


