  
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
profit_change = []


# Open and read CSV file

with open(csv_path, newline="") as csv_file:
    reader = csv.reader(csv_file, delimiter=",")

    # Skip the header row
    next(reader)

    # Loop through CSV file

    for row in reader:

        # Add date to month list
        months.append(row[0])

        # Add profit/loss value to profit_loss list
        profit_loss.append(int(row[1]))
 

# Calculate total number of months

total_months = (len(months))


# Calculate net total profit/losses over period

net_prof_loss = (sum(profit_loss))


# Calculate the changes in profit/losses over the period

for i in range(len(profit_loss)-1):
    profit_change.append(profit_loss[i+1]-profit_loss[i])
    

# Calculate the average of changes in profits/losses

av_pl_change = sum(profit_change) / len(profit_change)

# Calculate the greatest increase in profits

max_profit_increase = max(profit_change)


# Calculate the greatest decrease in losses




# Print results to terminal

    # Give text file the title 'Financial Analysis'. Print.

title = "Financial Analysis"

print(title)

title_line = "------------------------------"

print(title_line)

print("Total Months: " + str(total_months))

print(f"Total: ${round(net_prof_loss)}")

print(f"Average Change: ${av_pl_change: .2f}")

print(f"Max Profit Change: ${round(max_profit_increase)}")


# Write results to text file
text_file_title = ["Financial Analysis \n", "------------------------------ \n"]

with open(text_path, 'w') as f:
    f.writelines(text_file_title)
    f.write("Total Months: " + str(total_months))
    f.write('\n')
    f.write(f"Total: ${round(net_prof_loss)}")
    f.write('\n')
    f.write(f"Average Change: ${av_pl_change: .2f}")
