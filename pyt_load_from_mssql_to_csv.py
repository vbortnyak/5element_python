
import csv
import datetime
import pymssql
from decimal import Decimal



db_shema = ""
db_table = ""
db_full_table = ""
path_csv_file = "/home/msuser/"
# Cursor for get table list.
Tquery = "Select schemas.name as db_shema, tables.name as db_table from sys.tables INNER JOIN sys.schemas ON schemas.schema_id = tables.schema_id ORDER BY schemas.name, tables.name"

# Connect to MSSQL Server.
conn = pymssql.connect(server="192.168.183.144:1433",
                       user="sa",
                       password="12qwasZX",
                       database="TestDB")

# Create cursor for get table.
Tcursor = conn.cursor()
# execute query.
Tcursor.execute(Tquery)
# Get values from cursor.

rows = Tcursor.fetchall()
Tcursor.close()

#print(rows)

for row in rows:
    db_shema=row[0]
    db_table=row[1]
    #print(db_shema+"."+db_table)

# Create cursor
    cursor = conn.cursor()
# My query
    query = "Select * from "+db_shema+"."+db_table
# Execute query
    cursor.execute(query)

    path_csv_file_rez = path_csv_file+db_shema+"."+db_table+".csv"

    with open(path_csv_file_rez, 'w') as outfile:
        writer = csv.writer(outfile, delimiter=';', quoting=csv.QUOTE_NONE)
        for row in cursor:
             writer.writerow(row)

# Close the cursor and db_connection
    cursor.close()

conn.close()
