import pandas as pd
print("hello world")

#import csv
#with open(r"C:\Users\Admin\.ssh\QA-ProductDevDM05\Day 2\03_LibrarySystembook.csv", mode='r', newline='') as file:
#       reader = csv.reader(file)
        #for row in reader:
        #    print(row)  # row is a list of column values

def myFunction(arg1, arg2):
      #CODE
      output = "test func"
      print(output)
      return output

myFunction(1,2)

# Data engineering metrics (instantiation)
dropCount= 0

#Read the CSV file to clean it
data = pd.read_csv('data/03_Library Systembook.csv')

# Summary
print(f"There are {len(data)} rows in this dataset")
data.head()

# Converting the date of purchase to date format
#try: 
#    data['Book checkout'] = data['Book checkout'].str.replace('"', "", regex=True)
#    data['Book checkout'] = pd.to_datetime(data['Book checkout'], format='mixed' ) 
#    data.head()
#except Exception as e:
#    print(f"Error Occured: {e}")

# Investing the error
data.iloc[16]

# Invalid Rows
data.drop(16, inplace=True)
dropCount += 1

# RETRY Converting the date of purchase to date format
data['Book checkout'] = data['Book checkout'].str.replace('"', "", regex=True)
data['Book checkout'] = pd.to_datetime(data['Book checkout'], format='mixed' ) 
data['Book Returned'] = pd.to_datetime(data['Book Returned'], format='mixed' ) 
print(data.head())

na_dropped_data = data.dropna()
dropCount +=  len(data) - len(na_dropped_data)
na_dropped_data.head()

data

na_dropped_data

# Checking for duplicates
duplicate_data = na_dropped_data.duplicated()
duplicate_data.value_counts()

# Creating and using a function to enrich the data by adding in the time a book was on loan.
data_enriched = na_dropped_data.copy()

def enrich_dateDuration(colA, colB, df=data_enriched):
    """
    Takes the two input columns and the dataframe to create a new column date_delta which is the difference, in days, between colA and colB.
    
    Note: ColA should be the highest of the expected date columns.
    """
    df['date_delta'] = (df[colA]-df[colB]).dt.days
    return df.head()

#enrich_dateDuration(df=data_enriched, colA='Book Returned', colB='Book checkout')

print(enrich_dateDuration(df=data_enriched, colA='Book Returned', colB='Book checkout'))

data_enriched = na_dropped_data.copy()
data_enriched['loan_duration'] = (data_enriched['Book Returned'] - data_enriched['Book checkout']).dt.days
data_enriched.head()

valid_loan_data = data_enriched[data_enriched['loan_duration']>=0]
dropCount += len(data_enriched) - len(valid_loan_data)

valid_loan_data.head()

# Checking the length of this final dataset
valid_loan_data.shape[0]

# Final Drop Count
print(dropCount)

valid_loan_data.to_csv('load_data_cleaned.csv')

