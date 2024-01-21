import pandas as pd

data = {
    "Name": ["John", "Peter", "Loner", "Depressed"],
    "Age": [21, 18, 23, 18],
    "Address": ["Heaven", "USA", "Hell", "Void"],
    "Qualification": ["College Degree", "Graduated from a Bootcamp", "Failed social classes", "Passed University"]
}

df = pd.DataFrame(data)

print(df.loc[0: , ["Name", "Address"]])

''' 
print(object df goes there.)
Select Second to fourth column 

print(df[df.columns[1:4]]) 

df.columns[1:4] to obtain the column names at indices 1 to 3 (exclusive). df[df.columns[1:4]] displays the columns at given indices and including their rows. 

Select Multiple Columns in a Pandas Dataframe using loc[] function 

df.loc[1:3, ["Name", "Qualification"]] 
Another example 
df.loc[0, :] # is more flexible than basic df.columns method.
# Output: First column, all rows. 

# select all rows  

# select first two columns 

df.iloc[:, 0:2] 

# iloc[row slicing, column slicing] 

df.iloc[0:2, 1:3] 
'''
