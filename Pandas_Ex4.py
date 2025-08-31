import pandas as pd

# Suppose we have an Excel file named 'students.xlsx'
# Read the Excel file into a DataFrame
df = pd.read_excel('students.xlsx')

# Print the column names
print("Column Names:")
print(df.columns)
