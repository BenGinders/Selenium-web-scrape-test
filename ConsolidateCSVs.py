# Import libraries
import pandas as pd
import glob
import datetime

# Import files into a single dataframe
files = glob.glob('Files//*.csv')
df = pd.DataFrame()

#loop through the files and import
for f in files:
    csv = pd.read_csv(f)
    print(len(csv))
    df = df.append(csv)


df['Date'] = pd.to_datetime(df['Date'])
#df['date_int'] = pd.to_datetime(pd['date']).value

#df['intdate'] = pd.to_numeric(['Date'],downcast='integer')

print(df.head())
#Create a set of the date field to create discrete dates

dates = set(df['Date'])

for date in dates:
    print(type(date))
