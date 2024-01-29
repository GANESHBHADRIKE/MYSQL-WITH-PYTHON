import mysql.connector as connector

class DBhelper:
    #creating Table..........

    def __init__(self):
        self.con = connector.connect(host = 'localhost',port = '3306',user = 'root', password = 'Ganesh@12345',database = 'pythontest')
        query = 'create table if not exists user(userId int primary key, userName varchar(20),phone varchar(10))'
        cur = self.con.cursor()
        cur.execute(query)
        

    #inserting data into table..........
        
    def insert_user(self,userid, username, phone):
        query = "insert into user(userId,userName, phone) values ({}, '{}','{}')".format(userid,username,phone) 
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Entry has been done Successfully")

    # Fetching data.......
        
    def fetch_all(self):
        query = "select * from user"
        cur = self.con.cursor()    
        cur.execute(query)
        for row in cur:
            print("user id: ",row[0])
            print("user name: ",row[1])
            print("user phone: ",row[2])
            print()
        print("All data from DataBase")

    
    def update_user(self,userId,new_name,new_phone):
        query = "update user set userName = '{}', phone = '{}' where userId= {}".format(new_name,new_phone,userId) 
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Id has been updated Successfully..!!")

    
    def delete_user(self,userId):
        query = "delete from user where userId = {}".format(userId)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Deleted Successfully..!!")

