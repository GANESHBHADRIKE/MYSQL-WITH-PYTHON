import mysql.connector as connector

class DBhelper:
    #creating Table..........

    def __init__(self):
        self.con = connector.connect(host = 'localhost',port = '3306',user = 'root', password = 'Ganesh@12345',database = 'pythontest')
        query = 'create table if not exists user(userId int primary key, userName varchar(20),phone varchar(10))'
        cur = self.con.cursor()
        cur.execute(query)
        print("created")

    #inserting data into table..........
        
    def insert_user(self,userid, username, phone):
        query = "insert into user(userId,userName, phone) values ({}, '{}','{}')".format(userid,username,phone) 
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("user data enter successfully")

    # Fetching data.......
        
    def fetch_all(self):
        query = "select * from user where userName = 'Ganesh Bhadrike' "
        cur = self.con.cursor()    
        cur.execute(query)
        for row in cur:
            print("user id: ",row[0])
            print("user name: ",row[1])
            print("user phone: ",row[2])
            print()
            print()

    
    def update_user(self,userId,new_name,new_phone):
        query = "update user set userName = '{}',phone = '{}' where userId = {}".format(new_name,new_phone,userId)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()

        print("updated")




#create object of the class
helper = DBhelper()
helper.update_user(9820,"Ramesh Bhadrike","9819648908")
#helper.fetch_all()


# Using object of the class data has been inserted......

#helper.insert_user(9820,"Ganesh Bhadrike","9769348082")
# helper.insert_user(9788,"Shraddha Wagh","9004802510")
# helper.insert_user(9790,"Shweta Thike","9594065196")
# helper.insert_user(9819,"linda chandy","9535575710")

    





