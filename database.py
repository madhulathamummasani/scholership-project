import mysql.connector
class database:
    def connect(self):
        self.con=mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="scholarship"
        )
        self.cur=self.con.cursor()
    def add_student(self,roll_no,name,father_name,age,percentage,monthly_income,status):
        self.connect()
        self.cur.execute("insert into education values(%s,%s,%s,%s,%s,%s,%s )",(roll_no,name,father_name,age,percentage,monthly_income,status))
        self.con.commit()
        print("student details added successfully!")
        self.cur.close()
        self.con.close()
    def view_all_students(self):
        self.connect()
        self.cur.execute("select*from education")
        rows = self.cur.fetchall()  # Fetch all results here!

        if not rows:
            print("No student records found.")
            return

        for row in rows:
            # Assuming columns: roll_no, name, father_name, age, percentage, monthly_income, status
            print(f"Roll No: {row[0]}")
            print(f"Name: {row[1]}")
            print(f"Father Name: {row[2]}")
            print(f"Age: {row[3]}")
            print(f"Percentage: {row[4]}")
            print(f"Monthly Income: {row[5]}")
            print(f"Status: {row[6]}")
            print("---------------------------")

        # Now safe to close the cursor if needed
        self.cur.close()
        self.con.close()

    def delete_student(self,n):
        self.connect()
        self.cur.execute("delete from education where roll_no=%s",(n,))
        self.con.commit()
        print("Student Deleted successfully")
        self.cur.close()
        self.con.close()
    def view_status(self,roll_no):
        self.connect()
        self.cur.execute("select * from education where roll_no=%s",(roll_no,))
        row = self.cur.fetchone()

        print(f"Roll No: {row[0]}")
        print(f"Name: {row[1]}")
        print(f"Father Name: {row[2]}")
        print(f"Age: {row[3]}")
        print(f"Percentage: {row[4]}")
        print(f"Monthly Income: {row[5]}")
        print(f"Status: {row[6]}")
        print("---------------------------")
        self.con.commit()
        print("Student Deleted successfully")
        self.cur.close()
        self.con.close()
