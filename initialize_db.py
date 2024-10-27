import mysql.connector

#MySQL connection
sql= mysql.connector.connect(
  host="localhost",
  user="root", 
  passwd="granttheaccess"
)
my_con = sql.cursor()

#DataBase : Student
my_con.execute("Create database if not exists student")
my_con.execute("Use student")
#Table : Quiz List
my_con.execute("Create table if not exists quiz_list(id varchar(20), result int, time_remaining int)")
#Table : Answer Sheet
#could fit a 385-500 words answer and 77-100 words feedback
my_con.execute("Create table if not exists answer_sheet(id varchar(5), ans varchar(2500), marks int, feedback varchar(500))")

#DataBase : Teacher
my_con.execute("Create database if not exists teacher")
my_con.execute("Use teacher")
#Table : Quiz List
my_con.execute("Create table if not exists quiz_list(id varchar(20))")

#DataBase : Subject
my_con.execute("Create database if not exists subject")
my_con.execute("Use subject")
#Table : Quiz List
my_con.execute("Create table if not exists quiz_list(id varchar(20), status varchar(10), duration int, start time, end time, passwd varchar(127), date date, marks int, sections varchar(5))")
#Table : Question Paper
#could fit a 385-500 words long question and each option could fit 46-60 words
my_con.execute("Create table if not exists question_paper(id varchar(5), que varchar(1000), que_image longblob, a varchar(300), b varchar(300), c varchar(300), d varchar(300), marks int, ans varchar(4), grading_type varchar(10))")
#Table : Sections List
my_con.execute("Create table if not exists sections_list(section int)")
#Table : Student List
my_con.execute("Create table if not exists student_list(id varchar(10), name varchar(50))")