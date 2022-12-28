import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password="root",database="mydb")
mycur=mydb.cursor()
#Create Database
#mycur.execute("CREATE DATABASE mydb")
#Create Table
#s="CREATE TABLE cook(cookid integer(4),cookname varchar(50),cookprice float(5,2))"
#mycur.execute(s)
#Insert Data Into Database
#Insert Data in Single row
# query="INSERT INTO cook (cookid,cookname,cookprice) VALUES(%s,%s,%s)"
# c1=(1,"pk",250)
# mycur.execute(query,c1)
#insert data in Multiple Raw
# query="INSERT INTO cook (cookid,cookname,cookprice) VALUES(%s,%s,%s)"
# data=[(2,"gk",350),(3,"ck",540),(4,"lk",350)]
# mycur.executemany(query,data)
# mydb.commit()
#Extract data from table
# query="Select * From cook"
# mycur.execute(query)
# result=mycur.fetchall()
# for data in result:
#     print(data)
# #Update in table
# query="UPDATE cook SET cookprice=cookprice+10 where cookprice>=350"
# mycur.execute(query)
# mydb.commit()
#Delete data from Table
query="DELETE from cook where cookid=4"
mycur.execute(query)
mydb.commit()