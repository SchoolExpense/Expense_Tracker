from matplotlib import pyplot as plt
import numpy as np
import pandas as pd




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
        df['TExpense Category'] = exp_categories
        df['Item/Service Purchased'] = items_purchased
        df['Price'] = prices
        df['Date of Expense Purchase'] = dates
        
        #save the report
        df.to_csv('student_expense_report.csv')
        print(df)
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
                


#category = input("what category?")
# cat = ['Books', 'Pencils/Pens', 'Calculator','Food', 'Rent', 'Other']
# cat.append(category)

# expense = input("how much spent?")
# data = [70.00, 17.00, 35.00, 29.00, 1000.00, 41.00]
# data.append(expense)

# fig = plt.figure(figsize =(10, 7))
# plt.pie(data, labels = cat)

# plt.show()