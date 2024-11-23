import customtkinter as ctk
import mysql.connector

class Que:
    def __init__(self, id : int, db_connection, subject, exam, retest):
        self.db_connection = db_connection
        self.id = id
        self.que = None
        self.marks = None
        self.subject = subject
        self.exam = exam
        self.retest = retest

        #flags for checking is the widget was edited
        self.update_que = False
        self.update_marks = False

        from mcq import MCQ
        if not isinstance(self, MCQ):
            my_con = db_connection.cursor()

            if retest:
                self.exam = subject+"_"+exam
                my_con.execute("Use retest")
            else:
                my_con.execute("Use `{}`".format(subject))
        
            my_con.execute("insert into `{}`(id) values('{}')".format(self.exam,"OEQ"+str(self.id)))

            my_con.close()
    
    def show(self, frame):
        #functions to set flag True
        def que_edited():
            self.update_que = True
        def marks_edited():
            self.update_marks = True

        # Create the multi-line input Textbox for user to enter a question
        self.question_textbox = ctk.CTkTextbox(master=frame, width=200, height=200, font=("Sans Serif", 20), border_width=2)  # Increased height
        self.question_textbox.place(relx=0.455, rely=0.25, relwidth=0.75, relheight=0.4, anchor="center")  # Move slightly to the right
        if self.que:
            self.question_textbox.insert("1.0",self.que)
        self.question_textbox.bind("<KeyRelease>", que_edited)

        # Add a label for the question number to the left of the Textbox, aligned with the upper border
        question_label = ctk.CTkLabel(master=frame, text="Q"+str(self.id)+":", font=("Agency FB", 50, "bold"), anchor="e")  # Background color white
        question_label.place(relx=0.01, rely=0.09, anchor="w")  # Moved slightly further down (rely adjusted to 0.09)

        # Create the square-shaped entry box for marks to the right of the question textbox
        self.marks_entrybox = ctk.CTkEntry(master=frame, width=50, height=50, font=("Sans Serif", 20), justify="center",placeholder_text=self.marks)  # Width decreased
        self.marks_entrybox.place(relx=0.945, rely=0.0873, anchor="center")  # Moved slightly to the left and up
        self.marks_entrybox.bind("<KeyRelease>", marks_edited)

        marks_label = ctk.CTkLabel(master=frame, text="Marks:", font=("Agency FB", 39, "bold"), anchor="e")  # Background color white
        marks_label.place(relx=0.845, rely=0.0873, anchor="w")  # Moved slightly further down (rely adjusted to 0.09)

    def update(self):
        flag = False
        if self.update_que:
            flag = True
            self.que = self.question_textbox.get("1.0", "end-1c")
        if self.update_marks:
            flag = True
            self.marks = int(self.marks_entrybox.get())
        
        if flag:
            self.set()

    def set(self):
        my_con = self.db_connection.cursor()

        if self.retest:
            my_con.execute("Use retest")
        else:
            my_con.execute("Use '{}'".format(self.subject))
        
        my_con.execute("update '{}' set que = '{}', marks = {} where id = '{}'".format(self.exam,self.que,self.marks,"OEQ"+str(self.id)))

        my_con.close()