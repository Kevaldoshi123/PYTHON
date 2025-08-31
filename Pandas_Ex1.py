import pandas as pd

# Create a dictionary with student information
data = {
    'Student_ID': [1, 2, 3, 4, 5, 6],
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Emma', 'Frank'],
    'Age': [18, 17, 16, 18, None, 16],
    'Gender': ['Female', 'Male', 'Male', 'Female', 'Female', 'Male'],
    'Grade': ['A', 'B', 'C', 'A', 'B', None]
}

# Create a DataFrame
students_df = pd.DataFrame(data)

# Display the DataFrame

#print(students_df)

'''
missing_values = students_df.isnull()
print(missing_values)
'''



missing_values = students_df.isnull().sum()
print(missing_values)


