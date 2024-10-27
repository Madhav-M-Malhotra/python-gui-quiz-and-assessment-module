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