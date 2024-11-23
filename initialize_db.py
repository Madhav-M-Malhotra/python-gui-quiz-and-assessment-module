import customtkinter as ctk
import mysql.connector
from mysql.connector import Error

ctk.set_appearance_mode("light")#Set to light mode for white color scheme
ctk.set_default_color_theme("blue")

win = ctk.CTk()

win.title("MySQL Login")
win.geometry("400x190")

label = ctk.CTkLabel(win, text="Enter your MySQL Password", font=("Arial", 20))
label.pack(pady=10)

password_entry = ctk.CTkEntry(win, show="*", width=300, font=("Arial", 18), justify = "center")
password_entry.pack(pady=10)

login_button = ctk.CTkButton(win, text="Login", command=lambda:connect_to_mysql(), font=("Arial", 16))
login_button.pack(pady=10)

#Feedback label for connection errors
feedback_label = ctk.CTkLabel(win, text="", font=("Arial", 16))
feedback_label.pack(pady=10)  

def connect_to_mysql():
    password = password_entry.get()

    try:
        #Attempt MySQL connection
        connection = mysql.connector.connect(
            host="localhost",
            user="root",#Replace with your username
            password=password
        )
        if connection.is_connected():
            my_con = connection.cursor()

            #DataBase : Student 1
            my_con.execute("Create database if not exists AU4382917")
            my_con.execute("Use AU4382917")
            #Table : Quiz List
            my_con.execute("Create table if not exists quiz_list(id varchar(20), result int, time_remaining int)")
            #Table : Answer Sheet
            #could fit a 385-500 words answer and 77-100 words feedback
            my_con.execute("Create table if not exists answer_sheet(id varchar(5), ans varchar(2500), marks int, feedback varchar(500))")

            #DataBase : Student 2
            my_con.execute("Create database if not exists AU7625493")
            my_con.execute("Use AU7625493")
            #Table : Quiz List
            my_con.execute("Create table if not exists quiz_list(id varchar(20), result int, time_remaining int)")
            #Table : Answer Sheet
            #could fit a 385-500 words answer and 77-100 words feedback
            my_con.execute("Create table if not exists answer_sheet(id varchar(5), ans varchar(2500), marks int, feedback varchar(500))")

            #DataBase : Teacher
            my_con.execute("Create database if not exists `684237915`")
            my_con.execute("Use `684237915`")
            #Table : Quiz List
            my_con.execute("Create table if not exists quiz_list(id varchar(20))")

            #DataBase : Subject 1
            my_con.execute("Create database if not exists CSC210")
            my_con.execute("Use CSC210")
            #Table : Quiz List
            my_con.execute("Create table if not exists quiz_list(id varchar(20), status varchar(10), duration int, start time, end time, passwd varchar(127), date date, marks int, sections varchar(5))")
            #Table : Question Paper
            #could fit a 385-500 words long question and each option could fit 46-60 words
            my_con.execute("Create table if not exists question_paper(id varchar(5), que varchar(1000), a varchar(300), b varchar(300), c varchar(300), d varchar(300), marks int, ans varchar(4), grading_type varchar(10))")
            #Table : Sections List
            my_con.execute("Create table if not exists sections_list(section int)")
            my_con.execute("Insert ignore into sections_list values(1)")
            #Table : Section 1 Student List
            my_con.execute("Create table if not exists section_1(id varchar(10), name varchar(50))")
            my_con.execute("Insert ignore into section_1 values('AU4382917', 'Liam Parker'),('AU7625493', 'Sophia Bennett')")

            #DataBase : Subject 2
            my_con.execute("Create database if not exists MAT248")
            my_con.execute("Use MAT248")
            #Table : Quiz List
            my_con.execute("Create table if not exists quiz_list(id varchar(20), status varchar(10), duration int, start time, end time, passwd varchar(127), date date, marks int, sections varchar(5))")
            #Table : Question Paper
            #could fit a 385-500 words long question and each option could fit 46-60 words
            my_con.execute("Create table if not exists question_paper(id varchar(5), que varchar(1000), a varchar(300), b varchar(300), c varchar(300), d varchar(300), marks int, ans varchar(4), grading_type varchar(10))")
            #Table : Sections List
            my_con.execute("Create table if not exists sections_list(section int)")
            my_con.execute("Insert ignore into sections_list values(1),(2)")
            #Table : Section 1 Student List
            my_con.execute("Create table if not exists section_1(id varchar(10), name varchar(50))")
            my_con.execute("Insert ignore into section_1 values('AU4382917', 'Liam Parker')")
            #Table : Section 2 Student List
            my_con.execute("Create table if not exists section_2(id varchar(10), name varchar(50))")
            my_con.execute("Insert ignore into section_2 values('AU7625493', 'Sophia Bennett')")

            #DataBase : Retest
            my_con.execute("Create database if not exists retest")
            my_con.execute("Use retest")
            #Table : Quiz List
            my_con.execute("Create table if not exists quiz_list(id varchar(20), status varchar(10), duration int, start time, end time, passwd varchar(127), date date, marks int, sections varchar(5))")
            #Table : Question Paper
            #could fit a 385-500 words long question and each option could fit 46-60 words
            my_con.execute("Create table if not exists question_paper(id varchar(5), que varchar(1000), a varchar(300), b varchar(300), c varchar(300), d varchar(300), marks int, ans varchar(4), grading_type varchar(10))")
            #Table : Student List
            my_con.execute("Create table if not exists student_list(id varchar(10), name varchar(50))")
            
            connection.commit()
            connection.close()#Close the connection
            win.destroy()
    except Error as e:
        #Handle connection errors (like incorrect password)
        if e.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
            feedback_label.configure(text="Incorrect password. Please try again.", text_color="red")
            password_entry.delete(0, ctk.END)#Clear the password entry
        else:
            feedback_label.configure(text="Connection failed. Check your details.", text_color="red")

win.mainloop()