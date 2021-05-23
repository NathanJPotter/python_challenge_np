# This is a script to run an analysis of election_data for the PyPoll exercise

# Import the os module for creating file paths across operating systems. And import the module for reading CSV files

import os
import csv

# Specify os path for reading csv file

csv_path = os.path.join('..', 'PyPoll/Resources', 'election_data.csv')
print(csv_path)

# Specify os path for writing text file

text_path = os.path.join('..', 'PyPoll/Analysis', 'election_results.txt')
print(text_path)

# Give text file the title 'Election Results'. Print.

title = "Election Results"

print(title)

title_line = "------------------------------""------------------------------"

print(title_line)

# Write title to text file

text_file_title = ["Election Results \n", "------------------------------ \n"]

with open(text_path, 'w') as f:
    f.writelines(text_file_title)
