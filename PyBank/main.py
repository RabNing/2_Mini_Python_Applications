# Read data into Python from CSV file
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv
csvpath = os.path.join( 'Resources', 'budget_data.csv')
with open(csvpath) as csvfile:
# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")
    
    #Create empty lists
    month = []
    profit = []

    # Read each row of data after the header 
    #iterating over each row and append values to empty list
    for row in csvreader:
        month.append(row[0])
        profit.append(row[1])

    #Convert numbers in profit list from string to int
    profit_int= [eval(i) for i in profit]
    #print(profit_int)
  
    #Calc average change in profit and format the result
    avg_change = (profit_int[-1]-profit_int[0])/(len(month)-1)
    avg_change = round(avg_change,2)

    #Find the greatest increase and decrease in profits 
    Greatest_Inc = max(profit_int)
    Greatest_Dec = min(profit_int)

    #Zip the 2 lists into a dictionary:
    Dic = dict(zip(month,profit))
    #Find the months for greatest increase and decrease:
    GIM = max(Dic, key=Dic.get)
    GDM = min(Dic, key=Dic.get)
    print(Dic)

    #print list
    print("Financial Analysis")
    print("-------------------------------------")
    print("Total Months:", len(month))       
    print("Total: $",sum(profit_int))
    print("Average Change: $",avg_change)   
    print("Greatest Increase in Profits:", GIM ,"($", max(profit_int),")")
    print("Greatest Decrease in Profits:", GDM ,"($", min(profit_int),")")


    
      



        
    



        


        
        

