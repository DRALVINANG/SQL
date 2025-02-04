import sqlite3
import pandas as pd
import os

#------------------------------------------------------------------
# Step 1: Change Working Directory
#------------------------------------------------------------------
print("Current working directory:", os.getcwd())

# Set the working directory to your Desktop
os.chdir(r'C:\Users\DR ALVIN ANG\Desktop')

print("Current working directory:", os.getcwd())


#------------------------------------------------------------------
# Step 2: Read the Excel file
#------------------------------------------------------------------
file_path = r'C:\Users\DR ALVIN ANG\Desktop\world_data.xlsx'
xls = pd.ExcelFile(file_path)

#------------------------------------------------------------------
# Step 3: Connect to the SQLite database (create a new one or connect to an existing one)
#------------------------------------------------------------------
conn = sqlite3.connect(r'C:\Users\DR ALVIN ANG\Desktop\world_new.db')

#------------------------------------------------------------------
# Step 4: Loop through each sheet in the Excel file
#------------------------------------------------------------------
for sheet_name in xls.sheet_names:
    # Read each sheet into a DataFrame
    df = pd.read_excel(xls, sheet_name=sheet_name)
    
    # Convert the DataFrame to SQL (if the table already exists, this will replace it)
    df.to_sql(sheet_name, conn, if_exists='replace', index=False)

#------------------------------------------------------------------
# Step 5: Close the connection
#------------------------------------------------------------------
conn.close()

print(f"Data from {file_path} has been written to the new SQLite database 'world_new.db'")

