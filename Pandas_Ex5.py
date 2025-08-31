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


