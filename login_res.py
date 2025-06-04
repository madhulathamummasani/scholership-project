from database import*
class login_res:
    def __init__(self):
        self.database=database()
        self.login()
    def add(self):
        print("=========> ADD <========\n")
        roll_no=int(input("Enter the roll_no:"))
        name=input("Enter the Name:")
        father_name=input("Enter the Father Name:")
        age=int(input("Enter the age:"))
        percentage=float(input("Enter the percentage:"))
        monthly_income=float(input("Enter the the Monthly income:"))
        status=None
        if monthly_income<=300000:
            status="Accepted"
        elif 300000< monthly_income <=500000:
            status="Waiting"
        elif monthly_income>500000:
            status="Reject"
        self.database.add_student(roll_no,name,father_name,age,percentage,monthly_income,status)
        self.login_dashboard()

    def delete(self):
        n=int(input("Enter student roll num to delete: "))
        self.database.delete_student(n)
        self.login_dashboard()
    def view_all(self):
        print("=========> ALL STUDENTS <=========")
        self.database.view_all_students()
        self.login_dashboard()
    def view_status(self):
        try:
            roll_no = int(input("Enter roll number to view: "))
            self.database.view_status(roll_no)
        except ValueError:
            print("Invalid roll number.")
        self.login_dashboard()

    def login(self):
        print("=========> LOGIN <========\n")
        user="username"
        password_no="password"
        username=input("Enter your Username:")
        if username == user:
             print()
             password=input("Enter your Password:")
             if password==password_no:
                print("Login successfull")
                self.login_dashboard()
             else: print("wrong password")  
        else: 
            print("Ivalid credentials")
       
            
    def login_dashboard(self):
        print("======> SCHOLARSHIP <=========")
        print()
        print("1.ADD_STUDENT\n2.Delete\n3.VIEW ALL STUDENT\n4.VIEW STATUS\n")
        n=int(input("Enter the option:"))
        
        if n==1:
            self.add()
        elif n==2:
            self.delete()
        elif n==3:
            self.view_all()
        elif n==4:
            self.view_status()   
        elif n == 0:
            return
        else:
            print("Enter the correct option")
            self.login_dashboard()
obj=login_res()