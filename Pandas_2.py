import pandas as pd

# Dictionary containing student data
students = {
    'rollno': [1, 2, 3, 4, 5],
    'name': ['John', 'Alice', 'Bob', 'Emma', 'Michael'],
    'physics': [85, 90, 75, 88, 82],
    'maths': [95, 88, 92, 85, 90],
    'chemistry': [80, 85, 78, 90, 87]
}

# Creating DataFrame
df = pd.DataFrame(students)

# Printing the DataFrame
print(df)


=================

import pandas as pd

# Dictionary containing student data
students = {
    'rollno': [1, 2, 3, 4, 5],
    'name': ['John', 'Alice', 'Bob', 'Emma', 'Michael'],
    'physics': [85, 90, 75, 88, 82],
    'maths': [95, 88, 92, 85, 90],
    'chemistry': [80, 85, 78, 90, 87]
}

# Creating DataFrame
df = pd.DataFrame(students)

# Setting 'rollno' as index
df.set_index('rollno', inplace=True)

# Printing the DataFrame
print(df)


==========

import pandas as pd

# Dictionary containing student data
students = {
    'rollno': [1, 2, 3, 4, 5],
    'name': ['John', 'Alice', 'Bob', 'Emma', 'Michael'],
    'physics': [85, 90, 75, 88, 82],
    'maths': [95, 88, 92, 85, 90],
    'chemistry': [80, 85, 78, 90, 87]
}

# Creating DataFrame
df = pd.DataFrame(students)

# Adding a new column for total marks
df['total_marks'] = df['physics'] + df['maths'] + df['chemistry']

# Printing the DataFrame
print(df)


=============

import pandas as pd

# Dictionary containing student data
students = {
    'rollno': [1, 2, 3, 4, 5],
    'name': ['John', 'Alice', 'Bob', 'Emma', 'Michael'],
    'physics': [85, 90, 75, 88, 82],
    'maths': [95, 88, 92, 85, 90],
    'chemistry': [80, 85, 78, 90, 87]
}

# Creating DataFrame
df = pd.DataFrame(students)

# Deleting the 'chemistry' column
df.drop('chemistry', axis=1, inplace=True)

# Printing the DataFrame
print(df)


================

import pandas as pd

# Dictionary containing student data
students = {
    'rollno': [1, 2, 3, 4, 5],
    'name': ['John', 'Alice', 'Bob', 'Emma', 'Michael'],
    'physics': [85, 90, 75, 88, 82],
    'maths': [95, 88, 92, 85, 90],
    'chemistry': [80, 85, 78, 90, 87]
}

# Creating DataFrame
df = pd.DataFrame(students)

# Deleting the row with index label 2
df.drop(2, inplace=True)

# Printing the DataFrame
print(df)


================

import pandas as pd

# Dictionary containing student data
students = {
    'rollno': [1, 2, 3, 4, 5],
    'name': ['John', 'Alice', 'Bob', 'Emma', 'Michael'],
    'physics': [85, 90, 75, 88, 82],
    'maths': [95, 88, 92, 85, 90],
    'chemistry': [80, 85, 78, 90, 87]
}

# Creating DataFrame
df = pd.DataFrame(students)

# Adding a new column for total marks
df['total_marks'] = df['physics'] + df['maths'] + df['chemistry']

# Sorting DataFrame based on total marks
df_sorted = df.sort_values(by='total_marks', ascending=False)

# Printing the sorted DataFrame
print(df_sorted)


==============

import pandas as pd

# Dictionary containing student data
students = {
    'rollno': [1, 2, 3, 4, 5],
    'name': ['John', 'Alice', 'Bob', 'Emma', 'Michael'],
    'physics': [85, 90, 75, 88, 82],
    'maths': [95, 88, 92, 85, 90],
    'chemistry': [80, 85, 78, 90, 87]
}

# Creating DataFrame
df = pd.DataFrame(students)

# Finding the index of the student with the highest marks in maths
index_highest_maths = df['maths'].idxmax()

# Getting the name of the student with the highest marks in maths
name_highest_maths = df.loc[index_highest_maths, 'name']

# Printing the name of the student
print("Student with highest marks in Maths:", name_highest_maths)


================

import pandas as pd

# Dictionary containing student data
students = {
    'rollno': [1, 2, 3, 4, 5],
    'name': ['John', 'Alice', 'Bob', 'Emma', 'Michael'],
    'physics': [85, 90, 75, 88, 82],
    'maths': [95, 88, 92, 85, 90],
    'chemistry': [80, 85, 78, 90, 87]
}

# Creating DataFrame
df = pd.DataFrame(students)

# Using loc to target a specific column
physics_scores = df.loc[:, 'physics']

# Printing the targeted column
print(physics_scores)


===============

import pandas as pd

# Creating a DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}, index=['X', 'Y', 'Z'])

# Targeting a single column 'B'
column_B = df.loc[:, 'B']
print(column_B)


================

import pandas as pd

# Creating a DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}, index=['X', 'Y', 'Z'])

# Targeting multiple columns 'A' and 'C'
columns_A_C = df.loc[:, ['A', 'C']]
print(columns_A_C)


=============

import pandas as pd

# Creating a DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}, index=['X', 'Y', 'Z'])

# Targeting columns from 'A' to 'B'
columns_A_to_B = df.loc[:, 'A':'B']
print(columns_A_to_B)


=============

import pandas as pd

# Creating a DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}, index=['X', 'Y', 'Z'])

# Targeting a single value in column 'B' for row 'Y'
value_Y_B = df.loc['Y', 'B']
print(value_Y_B)


===========

Certainly! Here are some commonly used methods in pandas DataFrame:

1.  set_index : Set the DataFrame index (row labels) using one or more existing columns. This method can also remove the existing index if needed.

   Example:
     
   df.set_index('rollno', inplace=True)
    

2.  reset_index : Reset the DataFrame index to the default integer index (0, 1, 2, ...). This method can also remove the existing index if needed.

   Example:
     
   df.reset_index(inplace=True)
    

3.  head : Return the first n rows of the DataFrame. Default value of n is 5.

   Example:
     
   df.head()
    

4.  tail : Return the last n rows of the DataFrame. Default value of n is 5.

   Example:
     
   df.tail()
    

5.  info : Print a concise summary of a DataFrame, including the index dtype and column dtypes, non-null values, and memory usage.

   Example:
     
   df.info()
    

6.  describe : Generate descriptive statistics of the DataFrame's numeric columns, including count, mean, std, min, max, and quartiles.

   Example:
     
   df.describe()
    

7.  loc : Access a group of rows and columns by label(s) or a boolean array.

   Example:
     
   df.loc[1]  # Access row with index label 1
    

8.  iloc : Access a group of rows and columns by integer position(s).

   Example:
     
   df.iloc[0]  # Access first row of the DataFrame
    

9.  drop : Remove rows or columns by specifying labels.

   Example:
     
   df.drop('rollno', axis=1, inplace=True)  # Drop 'rollno' column
    

10.  groupby : Group DataFrame using a mapper or by a Series of columns.

    Example:
      
    df.groupby('name').mean()  # Group by 'name' and calculate mean for each group
     
