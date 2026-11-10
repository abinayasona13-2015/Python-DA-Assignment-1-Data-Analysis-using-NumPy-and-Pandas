import pandas as pd

# Define the data and custom indices
marks_data = [95, 92, 89, 85, 80]
custom_indices = ['Rank1', 'Rank2', 'Rank3', 'Rank4', 'Rank5']

# Create the Pandas Series
marks = pd.Series(marks_data, index=custom_indices)

print("Marks Series:")
print(marks)

import pandas as pd

# Define the marks Series with custom indices
marks = pd.Series([95, 92, 89, 85, 80], index=['Rank1', 'Rank2', 'Rank3', 'Rank4', 'Rank5'])

# 1. Access the 1st rank using integer position with .iloc
first_rank_mark = marks.iloc[0]
print("1st Rank Mark (position 0):", first_rank_mark)

# 2. Use .loc to retrieve by label name
top_three_loc = marks.loc['Rank1':'Rank3']
print("\nTop 3 Ranks (using .loc):\n", top_three_loc)

# 3. Use .iloc to retrieve the 3rd rank student (position 2)
third_rank_iloc = marks.iloc[2]
print("\n3rd Rank Mark (using .iloc):", third_rank_iloc)

# 4. Boolean mask for marks greater than 90
high_scorers = marks[marks > 90]
print("\nRanks with Marks > 90:\n", high_scorers)

import pandas as pd

# Assuming the marks Series is already defined:
# marks = pd.Series([95, 92, 89, 85, 80], index=['Rank1', 'Rank2', 'Rank3', 'Rank4', 'Rank5'])

# 1. Modify the mark of the 1st rank student to 100
marks['Rank1'] = 100
print("--- After Modifying 1st Rank ---")
print(marks)

# 2. Remove the entry corresponding to the last rank ('Rank5')
marks = marks.drop('Rank5')
print("\n--- After Removing the Last Rank ---")
print(marks)

# 3. Compute the CGPA by dividing each remaining mark in the Series by 10
cgpa = marks / 10
print("\n--- Computed CGPA (Marks / 10) ---")
print(cgpa)

import pandas as pd

# Define the data dictionary with all specified columns and rows
data = {
    'TransactionID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'ProductCategory': [
        'Electronics', 'Clothing', 'Electronics', 'Furniture', 
        'Clothing', 'Electronics', 'Furniture', 'Clothing', 
        'Furniture', 'Electronics'
    ],
    'Region': [
        'North', 'South', 'North', 'East', 'West', 
        'North', 'East', 'West', 'South', 'North'
    ],
    'Amount': [200, 150, 300, 450, 200, 250, 300, 180, 350, 400]
}

# Create the Pandas DataFrame
transactions = pd.DataFrame(data)

print("Transactions DataFrame:")
print(transactions)
print("\nDataFrame Shape:", transactions.shape)

import pandas as pd

# Assuming the transactions DataFrame is already defined:
# data = {
#     'TransactionID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
#     'ProductCategory': ['Electronics', 'Clothing', 'Electronics', 'Furniture', 'Clothing', 'Electronics', 'Furniture', 'Clothing', 'Furniture', 'Electronics'],
#     'Region': ['North', 'South', 'North', 'East', 'West', 'North', 'East', 'West', 'South', 'North'],
#     'Amount': [200, 150, 300, 450, 200, 250, 300, 180, 350, 400]
# }
# transactions = pd.DataFrame(data)

# --- 1. Basic Information and Inspection ---
print("--- DataFrame Head ---")
print(transactions.head())

print("\n--- DataFrame Tail ---")
print(transactions.tail())

print("\n--- Shape ---")
print(transactions.shape)

print("\n--- Column Names ---")
print(transactions.columns)

print("\n--- Data Types ---")
print(transactions.dtypes)

# --- 2. Display Specific Columns ---
print("\n--- ProductCategory and Amount Columns ---")
print(transactions[['ProductCategory', 'Amount']])

# --- 3. Retrieve the Last 3 Columns using iloc ---
# ':' means all rows, '-3:' means from the 3rd-to-last column to the end
print("\n--- Last 3 Columns ---")
print(transactions.iloc[:, -3:])

# --- 4. Filter Rows ('Region' == 'North' and 'Amount' > 200) ---
print("\n--- Filtered Rows (Region == 'North' and Amount > 200) ---")
filtered_transactions = transactions[(transactions['Region'] == 'North') & (transactions['Amount'] > 200)]
print(filtered_transactions)

# --- 5. Value Counts for ProductCategory ---
print("\n--- Product Category Value Counts ---")
print(transactions['ProductCategory'].value_counts())

# --- 6. Unique Values in Region ---
print("\n--- Unique Regions ---")
print(transactions['Region'].unique())

# --- 7. Group by Region and Find Mean Amount ---
print("\n--- Mean Amount by Region ---")
mean_amount_by_region = transactions.groupby('Region')['Amount'].mean()
print(mean_amount_by_region)

import pandas as pd

# Assuming the transactions DataFrame is already defined:
# data = {
#     'TransactionID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
#     'ProductCategory': ['Electronics', 'Clothing', 'Electronics', 'Furniture', 'Clothing', 'Electronics', 'Furniture', 'Clothing', 'Furniture', 'Electronics'],
#     'Region': ['North', 'South', 'North', 'East', 'West', 'North', 'East', 'West', 'South', 'North'],
#     'Amount': [200, 150, 300, 450, 200, 250, 300, 180, 350, 400]
# }
# transactions = pd.DataFrame(data)

# 1. Modify the 'Amount' for TransactionID 102 to 165
transactions.loc[transactions['TransactionID'] == 102, 'Amount'] = 165

# 2. Add a new column 'Discount' by calculating 10% of the 'Amount'
transactions['Discount'] = transactions['Amount'] * 0.10

print("--- After Modifying Amount & Adding Discount ---")
print(transactions.head())

# 3. Remove the row with TransactionID 109
row_index_109 = transactions[transactions['TransactionID'] == 109].index
transactions = transactions.drop(row_index_109)

# 4. Delete the 'Discount' column from the DataFrame
transactions = transactions.drop(columns=['Discount'])

print("\n--- Final Updated Transactions DataFrame ---")
print(transactions)