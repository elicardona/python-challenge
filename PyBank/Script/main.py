import os
import csv

csvpath = os.path.join("..", "Resources", "budget_data.csv")

total = 0
months = 0
sum_change = 0
previous = 0

change_list = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header=next(csvreader)

    for row in csvreader:

        total = total + float(row[1])
        months = months + 1
        if months > 1:   
            change = float(row[1]) -  previous
            sum_change = sum_change + change
            average_change = sum_change / 85 
            change_list.append(change)
        

        previous = float(row[1])
        
greatest_increase = max(change_list)
greatest_decrease = min(change_list)
print("Financial Analysis")
print("___________________________")
print(f"Total Months: {months}")
print(f"Total: {total}")
#print(sum_change)
print(f"Average Change: {average_change}")
print(f"Greatest Increase in Profit: {greatest_increase}")
print(f"Greatest Decrease in Profit: {greatest_decrease}")


with open("output.txt","w") as txt_file:

    txt_file.write("Financial Analysis\n")
    txt_file.write("___________________________\n")
    txt_file.write(f"Total Months: {months}\n")
    txt_file.write(f"Total: {total}\n")
    txt_file.write(f"Average Change: {average_change}\n")
    txt_file.write(f"Greatest Increase in Profit: {greatest_increase}\n")
    txt_file.write(f"Greatest Decrease in Profit: {greatest_decrease}\n")
