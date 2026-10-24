

import sqlite3 #importing SQLite

import hashlib #password hashing

conn = sqlite3.connect("student_management_system.db")
conn.execute("PRAGMA foreign_keys = ON")

#create cursor
cursor = conn.cursor()

# DATABASE DESIGN

#Create Tables
#1. users table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL)
''')



#2. students table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students(
        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER UNIQUE,
        name TEXT NOT NULL,
        age INTEGER,
        course TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(user_id) )
''')



#3. marks table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS marks(
        mark_id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER NOT NULL,
        subject TEXT NOT NULL,
        marks_obtained REAL NOT NULL,
        FOREIGN KEY (student_id) REFERENCES students(student_id))
''')


conn.commit()#save changes

print("All tables created successfully")

#PASSWORD HASHING 
#to secure password if db is stolen
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


#user registration
def register_user():

    print("------- REGISTRATION -------")
    username = input("Enter username: ")
    password = input("Enter password: ")

    if not username or not password:
        print("Username and password cannot be empty")
        return

    try:
        cursor.execute('''INSERT INTO USERS (username,password,role)
            VALUES(?,?,?)''',(username,hash_password(password),"student"))

        conn.commit()
        print("Registration Successful!!!\nYou are a student.")

    except sqlite3.IntegrityError:
        print("Username already exists!")

    except sqlite3.Error as error:
        print("Database error:", error)

#user login
def login_user():
    print("----------- LOGIN ----------- ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    if not username or not password:
        print("Username and password cannot be empty!")
        return None
    try:
        cursor.execute("""SELECT * FROM users 
        WHERE username = ?""", (username,))

        user = cursor.fetchone()

        if user and user[2] == hash_password(password):
            print("Login Successful!")
            print("Welcome", username)

            return {
                "user_id": user[0],
                "username": user[1],
                "role": user[3]
            }

        else:
            print("Invalid username or password!")
            return None
        

    except sqlite3.Error as error:
        print("Database error:", error)
        

#add student
def add_student(): 

    print("-------- ADD STUDENT --------") 

    username = input("Enter student's registered username: ").strip() 

    try:
        cursor.execute(""" SELECT user_id FROM users 
            WHERE username = ? AND role = ? """, (username, "student")) 
    
        user = cursor.fetchone() 
    
        if not user: 
            print("Student account not found! Register the student first.") 
            return 
        
        user_id = user[0] 

        # Check whether a profile already exists 
        cursor.execute(""" SELECT student_id FROM students 
            WHERE user_id = ? """, (user_id,)) 
        
        if cursor.fetchone():
            print("Student profile already exists!") 
            return 
        
        name = input("Enter student name: ").strip() 
        course = input("Enter course: ").strip() 
        
        if not name or not course: 
            print("Name and course cannot be empty!") 
            return 
        
        age = int(input("Enter age: ")) 
        
        if age <= 0: 
            print("Age must be greater than 0!") 
            return 
        
        cursor.execute(""" INSERT INTO students (user_id, name, age, course) 
            VALUES (?, ?, ?, ?) """, (user_id, name, age, course))
        
        conn.commit() 
        
        print("Student added successfully!") 
        
    except ValueError: print("Please enter a valid age!") 
    
    except sqlite3.Error as error: print("Database error:", error)


#view students
def view_students():

    print("\n---------- STUDENT RECORDS ----------")

    try:
        cursor.execute("""
            SELECT student_id, name, age, course
            FROM students
        """)

        students = cursor.fetchall()

        if not students:
            print("No student records found!")
            return

        for student in students:
            print(
                "ID:", student[0],
                "| Name:", student[1],
                "| Age:", student[2],
                "| Course:", student[3]
            )

    except sqlite3.Error as error:
        print("Database error:", error)

#search student
def search_student():

    print("\n--------- SEARCH STUDENT ----------")
    try:
        student_id = input("Enter student id: ")

        cursor.execute('''
            SELECT student_id, name, age, course FROM students WHERE student_id = ?''', (student_id,))

        student = cursor.fetchone()

        if student:
            print("ID: ",student[0],
                  "|Name: ",student[1],
                  "|Age: ",student[2],
                  "|Course: ",student[3])
        else:
            print("Student not found!")

    except ValueError:
        print("Enter valid student ID")

    except sqlite3.Error as error:
        print("Database error:", error)


#update student
def update_student():

    print("\n---------- UPDATE STUDENT ------------")

    try:
        student_id = int(input("Enter student ID: "))

        cursor.execute('''SELECT student_id FROM students 
            WHERE student_id = ?''',(student_id,))

        if cursor.fetchone() is None:
            print("Student not found!")
            return

        name = input("Enter new name: ").strip()
        course = input("Enter new course: ").strip()
        age = int(input("Enter new age: "))

        if not name or not course or age <= 0:
            print("Enter valid student details!")
            return
        cursor.execute("""UPDATE students SET name = ?, age = ?, course = ?
            WHERE student_id = ?""", (name, age, course, student_id))

        conn.commit()

        print("Student updated Successfully")

    except ValueError:
        print("Enter a valid name and student ID!")

    except sqlite3.Error as error:
        print("Database error:", error)


#DELETE STUDENT
def delete_student():
    print("\n----------- DELETE STUDENT -----------")

    try:
        student_id = int(input("Enter student ID: "))

        cursor.execute('''SELECT student_id FROM students 
            WHERE student_id = ?''',(student_id,))

        if cursor.fetchone() is None:
            print("Student not found!")
            return

        confirm = input("Delete this student? (yes/no): ").strip().lower()

        if confirm == "yes":
            cursor.execute('''DELETE FROM marks 
                WHERE student_id = ?''',(student_id,))

            cursor.execute('''DELETE FROM students 
            WHERE student_id = ?''',(student_id,))

            conn.commit()

            print("Student deleted successfully!")

        else:
            print("Deletion cancelled.")

    except ValueError:
        print("Enter a valid student ID!")

    except sqlite3.Error as error:
        conn.rollback()
        print("Database error:", error)


#add marks
def add_marks():
    print("\n----------- ADD MARK ------------")

    try:
        student_id = int(input("Enter student ID: "))
        subject = input("Enter subject: ").strip()
        marks = float(input("Enter marks: "))

        # Validate the marks
        if not subject:
            print("Subject cannot be empty!")
            return

        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100!")
            return

        # Check whether the student exists
        cursor.execute(
            "SELECT student_id FROM students WHERE student_id = ?",
            (student_id,)
        )

        if cursor.fetchone() is None:
            print("Student not found!")
            return

        # Insert marks using the correct column name
        cursor.execute("""
            INSERT INTO marks (student_id, subject, marks_obtained)
            VALUES (?, ?, ?)
        """, (student_id, subject, marks))

        conn.commit()
        print("Marks added successfully!")

    except ValueError:
        print("Please enter a valid student ID and marks!")

    except sqlite3.Error as e:
        print("Database error:", e)

#view marks
def view_marks():
    print("\n---------- VIEW MARKS ----------")

    student_id = input("Enter student ID: ")

    try:
        cursor.execute("""SELECT * FROM marks WHERE student_id = ?""",(student_id,))

        records = cursor.fetchall()

        if records:
            for record in records:
                print("Student Name:", record[0])
                print("Subject:", record[1])
                print("Marks:", record[2])
        else:
            print("No marks found for this student!")

    except sqlite3.Error as error:
        print("Database error:", error)

#update marks
def update_marks():
    print("\n---------- UPDATE MARKS ----------")

    try:
        mark_id = int(input("Enter mark ID: "))

        cursor.execute("SELECT * FROM marks WHERE mark_id = ?", (mark_id,))
        record = cursor.fetchone()

        if record is None:
            print("Mark ID not found!")
            return

        new_marks = float(input("Enter new marks: "))

        if new_marks < 0 or new_marks > 100:
            print("Marks must be between 0 and 100!")
            return

        cursor.execute(
            "UPDATE marks SET marks_obtained = ? WHERE mark_id = ?",
            (new_marks, mark_id)
        )

        conn.commit()
        print("Marks updated successfully!")

    except ValueError:
        print("Please enter valid numbers!")

    except sqlite3.Error as error:
        print("Database error:", error)



#DELETE MARK
def delete_marks():
    print("\n----------- DELETE MARKS ----------")

    try:
        mark_id = int(input("Enter mark ID: "))

        cursor.execute('''SELECT mark_id FROM marks WHERE mark_id = ?''',
            (mark_id,))

        if cursor.fetchone() is None:
            print("Mark record not found!")
            return

        cursor.execute('''DELETE FROM marks WHERE mark_id = ?''',
            (mark_id,))

        conn.commit()


        print("Marks deleted successfully!")

    except ValueError:
        print("Enter a valid mark ID!")

    except sqlite3.Error as error:
            print("Database error:", error)


#CREATING STUDENT MENU

def student_menu(user):

    while True:
        print("\n-=-=-=--=-- STUDENT MENU --=-=-=-=-")
        print("\n1. View Profile\n2. View Marks\n3. Logout")
        
        choice = input("Enter choice: ").strip()

        if choice == "1":
            cursor.execute("""SELECT student_id, name, age, course FROM students
            WHERE user_id = ?""", (user["user_id"],))

            student = cursor.fetchone()

            if student:
                print("Student ID:", student[0])
                print("Name:", student[1])
                print("Age:", student[2])
                print("Course:", student[3])
            else:
                print("Your student profile has not been created.")

        elif choice == "2":

            cursor.execute("""
            SELECT marks.subject, marks.marks
            FROM marks
            JOIN students
            ON marks.student_id = students.student_id
            WHERE students.user_id = ?
            """, (user["user_id"],))

            records = cursor.fetchall()

            if records:
                for record in records:
                    print("Subject:", record[0], 
                            "| Marks:", record[1])
            else:
                print("No marks found.")

        elif choice == "3":
            print("Logout successful!")
            break

        else:
            print("Invalid choice!")

#create admin
def create_admin():

    try:
        # Check whether an admin account already exists
        cursor.execute("""
            SELECT user_id FROM users
            WHERE role = 'admin'
        """)

        if cursor.fetchone():
            print("Admin account already exists!")
            return

        # Get admin login details
        print("\n-------- CREATE ADMIN ACCOUNT --------")

        username = input("Enter admin username: ").strip()
        password = input("Enter admin password: ").strip()

        if not username or not password:
            print("Username and password cannot be empty!")
            return

        # Save the admin account
        cursor.execute("""
            INSERT INTO users (username, password, role)
            VALUES (?, ?, ?)
        """, (username, hash_password(password), "admin"))

        conn.commit()

        print("Admin account created successfully!")

    except sqlite3.Error as error:
        print("Database error:", error)


#creating admin menu

def admin_menu():
    while True:
        print("\n=-=-=-=-=-- ADMIN MENU --=-=-=-=-=")

        print("\n1. Add student\n2. View students\n3.Search student\n4. Update student\n5.Delete student\n6.Add marks\n7. View marks\n8.Update marks\n9. Delete marks\n10. Logout")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_student()

        elif choice =="2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            add_marks()

        elif choice =="7":
            view_marks()

        elif choice == "8":
            update_marks()

        elif choice == "9":
            delete_marks()

        elif choice == "10":
            print("Logout successful!")
            break

        else:
            print("Invalid choice!")

#MAIN MENU
def main(): 
    while True: 
        print("\n") 
        print("=" * 40) 
        print("--------STUDENT MANAGEMENT SYSTEM --------") 
        print("=" * 40) 
        
        print("\n1. Register\n2. Login\n3. Exit") 
        
        choice = input("Enter choice: ").strip() 
        
        if choice == "1": 
            register_user() 
        
        elif choice == "2": 
            user = login_user() 
            
            if user: 
                if user["role"] == "admin": 
                    admin_menu() 
                    
                elif user["role"] == "student": 
                    student_menu(user) 
                    
                else: 
                    print("Unknown user role!") 
                    
        elif choice == "3": 
            print("Thank you for using the system!") 
            break 
        else: print("Invalid choice!") 
cursor.execute("PRAGMA table_info(marks)")
print(cursor.fetchall())

create_admin() 
main()
conn.close()














        


