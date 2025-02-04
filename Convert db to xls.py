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
# Step 2: Connect to the SQLite database
#------------------------------------------------------------------
conn = sqlite3.connect(r'C:\Users\DR ALVIN ANG\Desktop\world.db')

#------------------------------------------------------------------
# Step 3: List of table names
#------------------------------------------------------------------
table_names = ['City', 'Country', 'CountryLanguage']

#------------------------------------------------------------------
# Step 4: Create a Pandas Excel writer
#------------------------------------------------------------------
with pd.ExcelWriter('world_data.xlsx', engine='openpyxl') as writer:
    for table in table_names:
        # Read each table into a DataFrame
        query = f"SELECT * FROM {table}"
        df = pd.read_sql(query, conn)
        
        # Write DataFrame to a specific sheet
        df.to_excel(writer, sheet_name=table, index=False)

#------------------------------------------------------------------
# Step 5: Close the connection
#------------------------------------------------------------------
conn.close()

