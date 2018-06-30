#To export all tables as csv from a sql database
import mysql.connector as sql
import pandas as pd

dbname = 'test'	#Name of database
db_connection = sql.connect(host='localhost', database=dbname, user='root', password='') #Specify username and password

df1 = pd.read_sql('SHOW TABLES', con=db_connection)
tables_names = 'Tables_in_'+dbname
#print(df1.head())

for i in df1[tables_names]:
	query = 'SELECT * FROM '+i
	filename = i+'.csv'
	#print(i)
	df2 = pd.read_sql(query, con=db_connection)
	#print(df2)
	df2.to_csv(filename, index=False)
