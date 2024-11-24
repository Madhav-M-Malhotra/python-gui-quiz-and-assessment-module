import mysql.connector
from quelist import QueList

class Quiz:
    def __init__(self, db_connection, subject, exam, retest):
        self.id = exam
        self.mcq = QueList()
        self.oe = QueList()
        self.passwd = None
        self.schedule = None
        self.sections = None
        self.total_marks = None

        self.db_connection = db_connection
        self.subject = subject
        self.retest = retest

        my_con = db_connection.cursor()

        my_con.execute("Use `684237915`")

        if retest:
            my_con.execute("insert into quiz_list values(%s)",("retest_"+subject+"_"+exam))
            self.id = subject+"_"+exam
            my_con.execute("Use retest")
        else:
            my_con.execute("insert into quiz_list values('{}')".format(subject+"_"+exam))
            my_con.execute("Use `{}`".format(subject))
    
        my_con.execute("insert into quiz_list(id, status) values('{}', 'in making')".format(self.id))
        my_con.execute("Create table `{}`(id varchar(5), que varchar(1000), a varchar(300), b varchar(300), c varchar(300), d varchar(300), marks int, ans varchar(4), grading_type varchar(10))".format(self.id))

        my_con.close()