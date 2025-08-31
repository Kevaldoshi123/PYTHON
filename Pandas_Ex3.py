import pandas as pd

# DataFrame with student personal information
personal_info = {
    'Student_ID': [1, 2, 3, 4, 5],
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Emma'],
    'Age': [18, 17, 16, 18, 17],
    'Gender': ['Female', 'Male', 'Male', 'Female', 'Female']
}

df_personal = pd.DataFrame(personal_info)

# Display the original DataFrame
print("Original DataFrame:")
print(df_personal)


# Rename columns
df_renamed = df_personal.rename(columns={
    'Student_ID': 'ID',
    'Name': 'Full_Name',
    'Age': 'Student_Age',
    'Gender': 'Sex'
})

# Display the DataFrame with renamed columns
print("\nDataFrame with Renamed Columns:")
print(df_renamed)
print(df_renamed.columns)
