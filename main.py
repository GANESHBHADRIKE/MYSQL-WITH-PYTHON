from dbhelper import DBhelper

def main():

    while True:
        db = DBhelper()
        print("**************WELCOME**************")

        print("Press 1 to insert")
        print("Press 2 to fetch")
        print("Press 3 to update")
        print("press 4 to delete")
        print("Press 5 to exit")
        print()

        try:
            choose = int(input())
                
            if(choose == 1):
                #insert
                Id = int(input("Enter the new ID: "))
                Name = input("Enter the new name: ")
                phoneno = input("enter the new number: ")
                db.insert_user(Id,Name,phoneno)
                

            elif choose == 2:
                #fetch
                db.fetch_all()

            elif choose == 3:
                #update
                
                userId = input("Enter the user id you want to update: ")
                userName = input("Enter the user name you want to update: ")
                userPhone = input("Enter the user phone you want to update: ")
                db.update_user(userId,userName,userPhone)



            elif choose == 4:
                deleteid = int(input("enter the id you want to delete: "))
                db.delete_user(deleteid)
        
                
            elif choose == 5:
                break

            else:
                print("enter the valid user")

        except Exception as e:
            print(e)
            print("invalid input")

if __name__ == "__main__":
    main()


           







    





