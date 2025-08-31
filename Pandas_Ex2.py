import pandas as pd

# DataFrame with student personal information
personal_info = {
    'Student_ID': [1, 2, 3, 4, 5],
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Emma'],
    'Age': [18, 17, 16, 18, 17],
    'Gender': ['Female', 'Male', 'Male', 'Female', 'Female']
}

df_personal = pd.DataFrame(personal_info)

# DataFrame with student exam scores
exam_scores = {
    'Student_ID': [1, 2, 3, 4, 6],
    'Math': [95, 85, 78, 92, 88],
    'English': [88, 79, 85, 90, 87]
}

df_scores = pd.DataFrame(exam_scores)

# Display the original DataFrames
#print("Personal Information DataFrame:")
#print(df_personal)

#print("\nExam Scores DataFrame:")
#print(df_scores)

# Merge the DataFrames on the 'Student_ID' column
#merged_df = pd.merge(df_personal, df_scores, on='Student_ID', how='inner')

# Display the merged DataFrame
#print("\nMerged DataFrame (inner join):")
#print(merged_df)


'''
merged_outer = pd.merge(df_personal, df_scores, on='Student_ID', how='outer')
print("\nMerged DataFrame (outer join):")
print(merged_outer)
'''






'''
merged_left = pd.merge(df_personal, df_scores, on='Student_ID', how='left')
print("\nMerged DataFrame (left join):")
print(merged_left)
'''



'''
merged_right = pd.merge(df_personal, df_scores, on='Student_ID', how='right')
print("\nMerged DataFrame (right join):")
print(merged_right)

'''




