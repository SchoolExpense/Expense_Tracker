from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

expense_categories = { 'Education Materials': [], 'Transportation': [], 'Housing': [], 'Food': [], 'Entertainment': [] } #catergories for expenses


df = pd.DataFrame(data = expense_categories)  #use DataFrame as pandas object and pass expense_categories as the data (will be used for excel)

df.to_excel('student_expenses.xlsx') #create the excel file to use



# category = input("what category?")
# cat = ['Books', 'Pencils/Pens', 'Calculator','Food', 'Rent', 'Other']
# cat.append(category)

# expense = input("how much spent?")
# data = [70.00, 17.00, 35.00, 29.00, 1000.00, 41.00]
# data.append(expense)

# fig = plt.figure(figsize =(10, 7))
# plt.pie(data, labels = cat)

# plt.show()