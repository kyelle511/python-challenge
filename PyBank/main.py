import os
import csv


#path to collect the data
budget_csv=os.path.join("Resources","budget_data.csv")

#read in csv file
with open(budget_csv,'r') as csvfile:
#split data @ commas
    csvreader=csv.reader(csvfile,delimiter=",")
    header=next(csvreader)
    
   #setup counting variables and lists
    profit_list=[]
    months = []
    total_months=0
    net_profit=0
       
    for row in csvreader:
    #assign variables to names    
        date=str(row[0])
        profits=int(row[1])
    
    #create list of profit/losses
        profit_list.append(profits)
        months.append(date)

     #count the number of months (https://realpython.com/python-csv/)   
        total_months+=1
    
    #add each profit
        net_profit+=profits

#setup variables for determining changes
    change_list=[]
    total_changes=0
    x=0

#set up loop (thanks LA Robert Perron for helping me figure out the loop range correctly!)
    for x in range(len(profit_list)-1):
        change=(profit_list[x]-profit_list[x+1])*-1

#create a list of the changes in profit numbers
        change_list.append(change)

#add each change value to get running total
        total_changes+=change
        x+=1

#calcuate the greatest increase & decrease (https://www.geeksforgeeks.org/find-maximum-values-position-in-columns-and-rows-of-a-dataframe-in-pandas/)
        greatest_increase=max(change_list)
        greatest_decrease=min(change_list)

#find the corresponding month for the greatest increase
    index_of_greatest_increase = change_list.index(greatest_increase)
    month_of_greatest_increase = months[index_of_greatest_increase + 1]

#find the corresponding month for the greatest decrease
    index_of_greatest_decrease = change_list.index(greatest_decrease)
    month_of_greatest_decrease = months[index_of_greatest_decrease + 1]

#calculate the average change
    average_change=round(total_changes/(total_months-1),2)
        
#print results in the terminal
    print("Financial Analysis")
    print("--------------------------")
    print(f'Total Months: {str(total_months)}')
    print(f'Total: ${str(net_profit)}')
    print(f'Average Change: ${str(average_change)}')
    print(f'Greatest increase: {month_of_greatest_increase} - ${str(greatest_increase)}')
    print(f'Greatest decrease: {month_of_greatest_decrease} - ${str(greatest_decrease)}')

#printing results into a txt file (https://www.pythontutorial.net/python-basics/python-create-text-file/)
with open('analysis/analysis.txt','w') as f:
    print("Financial Analysis", file=f)
    print("--------------------------", file=f)
    print(f'Total Months: {str(total_months)}', file=f)
    print(f'Total: ${str(net_profit)}', file=f)
    print(f'Average Change: ${str(average_change)}', file=f)
    print(f'Greatest increase: {month_of_greatest_increase} - ${str(greatest_increase)}', file=f)
    print(f'Greatest decrease: {month_of_greatest_decrease} - ${str(greatest_decrease)}', file=f)
    f.close()