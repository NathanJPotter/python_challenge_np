# This is a script to run a financial analysis of budget_data for the PyBank exercise

# Import the os module for creating file paths across operating systems. And import the module for reading CSV files

import os
import csv

# Specify os path for reading csv file

csv_path = os.path.join('..', 'PyBank/Resources', 'budget_data.csv')
print(csv_path)

# Specify os path for writing text file

text_path = os.path.join('..', 'PyBank/Analysis', 'financial_analysis.txt')
print(text_path)

# Give text file the title 'Financial Analysis'. Print.

title = "Financial Analysis"

print(title)

title_line = "------------------------------""------------------------------"

print(title_line)

# Write title to text file

text_file_title = ["Financial Analysis \n", "------------------------------ \n"]

with open(text_path, 'w') as f:
    f.writelines(text_file_title)

# Calculate total number of months

with open(csv_path, newline= '') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
        break

    # Print and write to text file the total number of months


# Calculate net total profit/losses over period


    # Print and write to text file the total profit/losses


# Calculate the changes in profit/losses over the period



# Calculate the average of changes in profits/losses


    # Print and write to text file the average of changes in profits/losses


# Calculate the greatest increase in profits


    # Print and write to text file the greatest increase in profits


# Calculate the greatest decrease in losses


    # Print and write to text file the greatest decrease in losses


