import os

import csv

#loading files
csvpath = os.path.join("Resources", "budget_data.csv")
csvpath_out = os.path.join("Resources", "budget_data.txt")

#reading csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    

    #setting variables
    month_total = 0
    revenue = 0
    profit_change = 0
    greatest_increase = 0
    greatest_increase_month = ""
    greatest_decrease = 0
    greatest_decrease_month = ""
    change = 0


    #loop for getting total amounts needed
    for row in csvreader:
        month_total += 1
        revenue += int(row[1])

        #calculating the highest increase and decrease in profit
        if int(row[1]) - profit_change > greatest_increase:
            greatest_increase = int(row[1]) - profit_change
            greatest_increase_month = row[0]
        elif int(row[1]) - profit_change < greatest_decrease:
            greatest_decrease = int(row[1]) - profit_change
            greatest_decrease_month = row[0]
            change += int(row[1])

        profit_change = int(row[1])

avg_change = change / (month_total)
        
#gathering output
output = (f'Financial Analysis\n'
        f'--------------------------\n'
        f'Total Months: {month_total}\n'
        f'Total: ${revenue}\n'
        f'Average Change: {avg_change}\n'
        f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n'
        f'Greatest Increase in Profits: {greatest_decrease_month} (${greatest_decrease})\n')

print(output)

with open(csvpath_out, "w") as text_file:
    text_file.write(output)
    text_file.close()


















