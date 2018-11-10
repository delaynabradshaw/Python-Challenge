#import dependencies
import os
import csv
#read csv
csvpath = os.path.join('..','PyBank','Resources','budget_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    csv_header = next(csvreader)
    num_months = 0
    month = "0"
    net_profit_loss = 0
    profit_loss_change = 867884
    month_change = 0
    total_month_changes = 0
    profit_greatest = 0
    name_greatest = "0"
    profit_decrease = 0
    name_least = "0"
    for row in csvreader:
#the total number of months included in the dataset
        if month != row[0]:
            num_months = num_months + 1
#the total net amount of "Profits/Losses" over the period
        net_profit_loss = net_profit_loss + int(row[1])
#the average change in "Profit/Losses" between months over the entire period
        if profit_loss_change != row[1]:
            month_change = int(row[1]) - int(profit_loss_change)
            total_month_changes = total_month_changes + month_change
            profit_loss_change = row[1]
#the greatest increase in profits (date and amount) over the entire period
            if profit_greatest < month_change:
                profit_greatest = month_change
                name_greatest = row[0]
#the greatest decrease in losses (date and amount) over the entire period
            if profit_decrease > month_change:
                profit_decrease = month_change
                name_least = row[0]
#print all the data
average_month_changes = total_month_changes/85
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {num_months}")
print(f"Total: ${net_profit_loss}")
print(f"Average  Change: ${average_month_changes}")
print(f"Greatest Increase in Profits: {name_greatest} ({profit_greatest})")
print(f"Greatest Decrease in Profits: {name_least} ({profit_decrease})")
#export a text file of the results
def outputfile():
    outputname = 'financial_analysis.txt'
    myfile = open(outputname, 'w')
    myfile.write('Financial Analysis')
    myfile.write('----------------------------')
    myfile.write(f'Total Months: + {num_months}')
    myfile.write(f'Total: ${net_profit_loss}')
    myfile.write(f'Average Change: ${average_month_changes}')
    myfile.write(f'Greatest Increase in Profits: {name_greatest} ({profit_greatest})')
    myfile.write(f'Greatest Decrease in Profits: {name_least} ({profit_decrease})')
    myfile.close()
outputfile()
