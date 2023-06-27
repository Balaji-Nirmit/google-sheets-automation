# OM GANGANPATAY NAMAH
# HAR HAR MAHADEV
# JAI SHRI RAM
# pip install gspread
# pip install oauth2client
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import csv

scope=["https://www.googleapis.com/auth/spreadsheets",
      "https://www.googleapis.com/auth/drive"]

credentials=ServiceAccountCredentials.from_json_keyfile_name('credentials.json',scope)
client =gspread.authorize(credentials)

# to create a file 
# client.create("FirstSheet")  #this way will create first sheet in client email only

#to show in your email do the 2 down steps 
# sheet=client.create("firstshet")
# sheet.share("myemail@gmail.com",perm_type='user',role='writer')
sheet=client.open("firstshet").sheet1

df=pd.read_csv("california_housing_test.csv")

# df.columns.values.tolist()    to store column name
# df.values.tolist()   to store data

sheet.update([df.columns.values.tolist()]+df.values.tolist())

# the above way we can write the data into the sheet without loosing the previous data if executed the program multiple times.

# to delete the rows
# sheet.delete_row(n) n is number of rows
# sheet.clear() to clear complete file




# to download as csv file
sheet = client.open('firstshet').sheet1
csv_file = sheet.get_all_values()
with open('output.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(csv_file)
