import pandas as pd


'''
df = pd.read_csv("C:\\Users\\Keval Doshi\\OneDrive\\Desktop\\Study materials\\Python\\data.csv")
print(df)

print( type(df) )

print(pd.options.display.max_rows) 
'''


# openpyxl : pip install openpyxl

'''
df = pd.read_excel( "C:\\Users\\Keval Doshi\\OneDrive\\Desktop\\Study materials\\Python\\Pandaexcel.xlsx" )
print(df)
print( type(df) )
'''

'''
df = pd.read_excel( "C:\\Users\\Keval Doshi\\OneDrive\\Desktop\\Study materials\\Python\\Pandaexcel.xlsx",sheet_name = "Sheet2" )
print(df)
'''

'''
df = pd.read_excel( "C:\\Users\\Keval Doshi\\OneDrive\\Desktop\\Study materials\\Python\\Pandaexcel.xlsx",sheet_name = 1 )
print(df)
'''


'''
df_dict = pd.read_excel( "C:\\Users\\Keval Doshi\\OneDrive\\Desktop\\Study materials\\Python\\Pandaexcel.xlsx",sheet_name = ["Sheet1","Sheet2"])
#print(df_dict)

print( df_dict["Sheet1"] )
'''



'''
df_dict =    pd.read_excel( "C:\\Users\\Keval Doshi\\OneDrive\\Desktop\\Study materials\\Python\\Pandaexcel.xlsx",sheet_name = ["Sheet1","Sheet2"])


df1 = df_dict["Sheet1"]
df2 =  df_dict["Sheet2"]

print(df1)

'''


'''
df_dict =    pd.read_excel( "C:\\Users\\Keval Doshi\\OneDrive\\Desktop\\Study materials\\Python\\Pandaexcel.xlsx",sheet_name = None )
print(df_dict)
'''

'''
df =    pd.read_excel( "C:\\Users\\Keval Doshi\\OneDrive\\Desktop\\Study materials\\Python\\Pandaexcel.xlsx",names = ["Id","Student Name","age"] )
print(df)

'''


'''
df =    pd.read_excel( "C:\\Users\\USER\\Music\\Book1.xlsx",usecols = ["rollno","name"] )
print(df)
'''

'''
df =    pd.read_excel( "C:\\Users\\USER\\Music\\Book1.xlsx",header = 2 )
print(df)
'''

'''
df =    pd.read_excel( "C:\\Users\\USER\\Music\\Book1.xlsx",header = None )
print(df)

'''


'''
df =    pd.read_excel( "C:\\Users\\USER\\Music\\Book1.xlsx",header = [0,1] )
print(df)
'''

















