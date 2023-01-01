import mysql.connector as mycon
con=mycon.connect(host="localhost",user="root",password="root",database="mydb")


try:
    if(con):
        print("connection is Sucessfull")
        mycur=con.cursor()
except:
    print("Something went wrong")   

 #....................Insert............................
def insert():
    # cookid=input("Enter cookid:")
    cookname=input("Enter cookname:")
    cookprice=input("Enter cookprice:")
    query="iNSERT INTO cook(cookname,cookprice) VALUES(%s,%s)"
    data=(cookname,cookprice)
    try:
        mycur.execute(query,data)
        con.commit()
        print("Data inserted")
        menu()
    except Exception as e:
        print(e)
        menu()

        #..........................Read Section...........................

def read():
    query="SELECT * FROM cook"
    try:
        mycur.execute(query)
        result=mycur.fetchall()
        for data in result:
            print(data)
        print("sucessfull")
        print("=====================")
        menu()
    except:
        print("Error Occured")
        menu()


# def delete():
#     rowid=input("Enter row id want to delete: ")
#     query="delete from cook WHERE cookid="+rowid
#     try:
#         mycur.execute(query)
#         con.commit()
#         print("ROW DELETED")
#         menu()
#     except:
#         print("Error")
#         menu()

#2nd method to delete 
#.......................Delete......................................
def delete():
    ch=input("Do you have row_id?(y/n): ").lower()
    if(ch=='y'):
        id=(input("Enter your row id: "))
        query="DELETE FROM cook WHERE cookid="+id
        try:
            mycur.execute(query)
            con.commit()
            print("Row Deleted")
            menu()
        except:
            print("Error")
            menu()
    else:
        print("Go to read section and get your id")
        menu()
         
def get_by_id(self,id):
 
    pass

#.................Update Section...................
def update():
    ch=input("Do you have row id ? (y/n)").lower()
    if(ch=='y'):
        id=input("Enter your row id:")
        new_cook_name=input("Enter new name:")
        new_cook_price=input("Enter New cook Price:")
        try:
          query="Update cook Set cookname=%s,cookprice=%s Where cookid=%s"
          val=(new_cook_name,new_cook_price,id)
          mycur.execute(query,val)
          con.commit()
          print("Updation sucessfull")
          menu()
        except:
            print("Error Occured")
            menu()
    else:
        print("Error Occured")
        menu()

        #...............Menu Section......................  
        
def menu():
    print("Please Select any option:\n1.INSERT\n2.READ \n3.UPDATE \n4.DELETE \n5.Exit")
    choice=int(input("Enter your Choice:"))
    if(choice==1):
        insert()
    elif(choice==2):
        read()
    elif(choice==3):
        update()
    elif(choice==4):
        delete()
    elif(choice==5):
        exit()
    else:
        print("Please Enter valid Choice")
        menu()
menu()