from matplotlib import pyplot as plt
import numpy as np

category = input("what category?")
cat = ['Books', 'Pencils/Pens', 'Calculator','Food', 'Rent', 'Other']
cat.append(category)

expense = input("how much spent?")
data = [70.00, 17.00, 35.00, 29.00, 1000.00, 41.00]
data.append(expense)

fig = plt.figure(figsize =(10, 7))
plt.pie(data, labels = cat)

plt.show()