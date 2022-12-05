from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import math




#exp_categories = ["Education Materials", "Housing", "Transportation", "Clothing", "Food", "Bills", "Entertainment/Misc"]  #list to store category names


    
#empty sub-lists for actual expenses    
items_purchased = []
prices = []
dates = []
exp_categories = [] #tentative list


#function for adding the expense
def add_expense(category, item, price, date):
    exp_categories.append(category)
    items_purchased.append(item)
    prices.append(price)
    dates.append(date)
    

budget = float(input("Enter your Budget: "))


#main begins below
choice = -1  #user input

while(choice != 0):
    print("\n\nStudent Expense Tracker Main Menu")
    print("Choose an Option Below")
    print("------------------------------------")
    print("1) Enter an Expense Under EDUCATION MATERIALS")
    print("2) Enter an Expense Under HOUSING")
    print("3) Enter an Expense Under TRANSPORTATION")
    print("4) Enter an Expense Under CLOTHING")
    print("5) Enter an Expense Under FOOD")
    print("6) Enter an Expense Under BILLS")
    print("7) Enter an Expense Under ENTERTAINMENT/MISC") 
    print("8) Show and Save Expense Report")
    print("9) Visualize Expense Report")
    print("0) EXIT")
    choice = int(input("Please Make Your Selection: "))
    if(choice == 0):
        break
    if(choice == 1):
        category = "EDUCATION MATERIALS"
    elif(choice == 2):
        category = "HOUSING"
    elif(choice == 3):
        category = "TRANSPORTATION"
    elif(choice == 4):
        category = "CLOTHING"
    elif(choice == 5):
        category = "FOOD"
    elif(choice == 6):
        category = "BILLS"
    elif(choice == 7):
        category = "ENTERTAINMENT/MISC"
    elif(choice == 8):
        print("Saving...")
        df = pd.DataFrame()
        df['Expense Category'] = exp_categories
        df['Item/Service Purchased'] = items_purchased
        df['Price'] = prices
        df['Date of Expense Purchase'] = dates
        
        #save the report
        df.to_csv('student_expense_report.csv')
        print(df)
        
        #test the sums
        sum_edu = df.loc[df['Expense Category'] == 'EDUCATION MATERIALS', 'Price'].sum()
        sum_housing = df.loc[df['Expense Category'] == 'HOUSING', 'Price'].sum()
        sum_trans = df.loc[df['Expense Category'] == 'TRANSPORTATION', 'Price'].sum()
        sum_cloth = df.loc[df['Expense Category'] == 'CLOTHING', 'Price'].sum()
        sum_food = df.loc[df['Expense Category'] == 'FOOD', 'Price'].sum()
        sum_bills = df.loc[df['Expense Category'] == 'BILLS', 'Price'].sum()
        sum_misc = df.loc[df['Expense Category'] == 'ENTERTAINMENT/MISC', 'Price'].sum()
        total_sum = sum_edu + sum_housing + sum_trans + sum_cloth + sum_food + sum_bills + sum_misc
        
        print()
        print('Expense Totals by Category')
        print('-----------------------------------------------------------')
        print('EDUCATION MATERIALS: $' + str("%.2f" % sum_edu))
        print('HOUSING: $' + str("%.2f" % sum_housing))
        print('TRANSPORTATION: $' + str("%.2f" % sum_trans))
        print('CLOTHING: $' + str("%.2f" % sum_cloth))
        print('FOOD: $' + str("%.2f" % sum_food))
        print('BILLS: $' + str("%.2f" % sum_bills))
        print('ENTERTAINMENT/MISC: $' + str("%.2f" % sum_misc))
        print('-----------------------------------------------------------')
        print('TOTAL SUM OF EXPENSES: $' + str("%.2f" % total_sum))  #.2f gives 2 decimal points format
        
        
        result = budget - total_sum
        
        print('NET AMOUNT BASED ON BUDGET: $' + str("%.2f" % result))
        
    elif(choice == 9):
        '''def unique(category):
            uni=[]
            for x in category:
                if x not in uni:
                    uni.append(x)'''

        report = pd.read_csv("student_expense_report.csv")  # reading csv
        category = report['Expense Category'].tolist()  # parsing column to list
        expense = report['Price'].tolist()  # parsing column to list

        dfn = pd.DataFrame(category, columns=['category'])
        dfn['sum'] = pd.DataFrame(expense)
        dfn_sum = dfn.groupby(['category'], group_keys=True).sum()
        sum = dfn_sum['sum'].tolist()

        dfn.groupby(['category']).sum().plot(kind='pie', y='sum', legend=False, ylabel="", autopct='%1.0f%%')
        plt.show()

    else:
        print("INVALID SELECTION! PLEASE CHOOSE A VALID OPTION")        
    
    #user enters item purchased and expense price
    if (choice == 1 or choice == 2 or choice == 3 or choice == 4 or choice == 5 or choice == 6 or choice == 7):
        item = input('Enter the Item/Service that was Purchased Under Expense Category ' + category + ': ')
        price = float(input('Enter the Price of the Item/Service: '))
        date_purchased = input("Enter the Date of the Expense/Purchase (mm/dd/yy) or N/A if Unknown: ")
        add_expense(category, item, price, date_purchased)          
                
#print new line for formatting purposes
print()                
                



