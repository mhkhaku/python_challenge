# task is to create a Python script that analyzes the records to calculate each of the following values:

# The total number of months included in the dataset

# The net total amount of "Profit/Losses" over the entire period

# The changes in "Profit/Losses" over the entire period, and then the average of those changes

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in profits (date and amount) over the entire period


import os
import csv

budget_data = os.path.join('Resources', 'budget_data.csv')

with open (budget_data,'r') as pybank:
    csv_reader = csv.reader(pybank, delimiter=",")
    csv_header = next(pybank)
    print(f"Header: {csv_header}")

    month_count = list(csv_reader)
    total_month = len(month_count)

# The total number of months included in the dataset


    print(f"Total Months: {total_month}")

    net_profit = 0
    diff = []
    months=[]


    for row in month_count:
        net_profit += int(row[1])
        months.append (row[0])
    
    my_currency = net_profit
    desired_representation = "{:,}".format(my_currency)

# The net total amount of "Profit/Losses" over the entire period

    
    print(f"Net Total Amount: $ {desired_representation}")

# The changes in "Profit/Losses" over the entire period, and then the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire period

    sumdiff = 0
    for row in range(total_month-1):
        diff.append(int(month_count[row+1][1])-int(month_count[row][1]))
    
    maxdiff = diff[0]
    maxmonth = 0

    mindiff = diff[0]
    minmonth=0

    for i in range(len(diff)):
        if diff[i]>maxdiff:
            maxdiff = diff[i]
            maxmonth = i
        if diff[i] < mindiff:
            mindiff = diff[i]
            minmonth = i
        

sumdiff = sum(diff)
average = sumdiff/(total_month-1)
print("The average difference for months $" + str(round(average,2)))
print(f"The greatest increase in profits is {months[maxmonth+1]} (${str(maxdiff)})")
print(f"The greatest increase in profits is {months[minmonth+1]} (${str(mindiff)})")

# export a text file with the results.

pybankfile = open("pybank.txt",'w')
pybankfile.write("Financial Analysis\n")
pybankfile.writelines("--------------------------------------\n")
pybankfile.writelines((f"Total Months: {total_month}"))
pybankfile.write("\n")
pybankfile.writelines("--------------------------------------\n")
pybankfile.writelines("The average difference for months $" + str(round(average,2)))
pybankfile.write("\n")
pybankfile.writelines(f"The greatest increase in profits is {months[maxmonth+1]} (${str(maxdiff)})")
pybankfile.write("\n")
pybankfile.writelines(f"The greatest increase in profits is {months[minmonth+1]} (${str(mindiff)})")
pybankfile.write("\n")
pybankfile.writelines("--------------------------------------\n")