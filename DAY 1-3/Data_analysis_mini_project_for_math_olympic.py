import pandas as pd 
import openpyxl
import numpy

olympic=pd.read_excel(r'C:\Users\omar2\Music\olympice.xlsx')
print(olympic)
# This program is based on the excel program that i have provided
#lets start the analysis
#at first who have got more than 60
print("\n\nlets see who have got more than 60\n\n")
number_60=olympic[olympic['Number']>60]
print(number_60)
print("\n\nLets see who have got more than 60 in less than 65 minutes\n\n")
numner_time=olympic[(olympic['Number']>60)&(olympic['Time']<65)]
print(numner_time)
print("\n\nThose who have participated in under class 10\n\n")
junior=olympic[olympic['Class']<10]
print(junior)
print("\n\n Lets see who have got the highest number between class 6 to 10\n\n")
junior_highest=junior.loc[junior['Number'].idxmax()]
print(junior_highest)
print("\n\nThe Senior who have participated\n\n")
senior=olympic[olympic['Class']>9]
print(senior)
print("\n\nThe person who have got the highest number is\n\n")
senior_highest=senior.loc[senior['Number'].idxmax()]
print(senior_highest)
print("\n\nWho have got highest number in the lowest time\n\n")
highest_min_time=olympic.loc[(olympic['Number'].idxmax())&(olympic['Time'].idxmin())]
print(highest_min_time)
print("\n\nThe most junior with high mark is\n\n")
most_junior=olympic.loc[(olympic['Age'].idxmin())&(olympic['Number'].idxmax())]
print(most_junior)
print("\n\nIts time for the sudent who have got highest in the tournament\n\n")
highest=olympic.loc[olympic['Number'].idxmax()]
print(highest)
