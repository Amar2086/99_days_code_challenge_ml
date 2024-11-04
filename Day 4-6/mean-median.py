import pandas as pd 
import openpyxl

number1 = pd.read_excel(r'D:\99 Days Code Challenge Machine Learning\DAY 1-3\olympice.xlsx')

mean_number=number1['Number'].mean()
print(mean_number)
average_age=number1['Age'].mean()
print(average_age)
average_time=number1['Time'].mean()
print(average_age)
print("Median of the number is")
median_number=number1['Number'].median()
print(median_number)