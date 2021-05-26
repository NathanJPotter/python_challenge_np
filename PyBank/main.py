# This is a script to run a financial analysis of budget_data for the PyBank exercise

# Import the os module for creating file paths across operating systems. And import the module for reading CSV files

import os
import csv

# Specify os path for reading csv file

csv_path = os.path.join('..', 'PyBank/Resources', 'budget_data.csv')

# Specify os path for writing text file

text_path = os.path.join('..', 'PyBank/Analysis', 'financial_analysis.txt')


# Create lists to hold data

months = []
profit_loss = []


# Calculate total number of months

with open(csv_path, newline="") as csv_file:
    reader = csv.reader(csv_file)
    header = next(reader)
    lines = len(list(reader))
    total_months = "Total Months: " + str(lines)
 





# Calculate net total profit/losses over period




# Calculate the changes in profit/losses over the period




# Calculate the average of changes in profits/losses




# Calculate the greatest increase in profits




# Calculate the greatest decrease in losses


# Print results to terminal

    # Give text file the title 'Financial Analysis'. Print.

title = "Financial Analysis"

print(title)

title_line = "------------------------------"

print(title_line)

print(total_months)

# Write results to text file
text_file_title = ["Financial Analysis \n", "------------------------------ \n"]

with open(text_path, 'w') as f:
    f.writelines(text_file_title)
    f.write(total_months)
    f.write('\n')