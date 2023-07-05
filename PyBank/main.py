import os
import csv

budget_data_csv = os.path.join(".","Resources","budget_data.csv")

count = 0
net_total = 0
past_profit_loss = 0
total_change = 0
greatest_increase = 0
greatest_increase_date = ""
greatest_decrease = 0
greatest_decrease_date = ""

with open(budget_data_csv,'r') as file:
    filereader = csv.reader(file,)

    header = next(filereader)

    for row in filereader:
        count += 1
        profit_loss = int(row[1])
        net_total += profit_loss
        
        if count > 1:
            change = profit_loss - past_profit_loss
            total_change += change
            
            if count > 1:
                change = profit_loss - past_profit_loss
                total_change += change

                if change > greatest_increase:
                    greatest_increase = change
                    greatest_increase_date = row[0]
                if change < greatest_decrease:
                    greatest_decrease = change
                    greatest_decrease_date = row[0]
            
        past_profit_loss = profit_loss
        
average_change = total_change / (count - 1)




print("Total Months:", count)
print("Total: $"+str(net_total))
print("Average Change: $"+str(round(average_change, 2)))
print("Greatest Increase in Profits:", greatest_increase_date, "($", greatest_increase, ")")
print("Greatest Decrease in Profits:", greatest_decrease_date, "($", greatest_decrease, ")")





