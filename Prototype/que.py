import customtkinter as ctk

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

            self.db_connection.commit()
            my_con.close()

    @property
    def ready_for_scheduling(self):
        if self.que and self.marks:
            return True
    
    def show(self, frame):
        #functions to set flag True
        def que_edited(*args):
            self.update_que = True
        def marks_edited(*args):
            self.update_marks = True

        self.question_textbox = ctk.CTkTextbox(master=frame, width=200, height=200, font=("Sans Serif", 20), border_width=2)
        self.question_textbox.place(relx=0.455, rely=0.25, relwidth=0.75, relheight=0.4, anchor="center")
        if self.que:
            self.question_textbox.insert("1.0",self.que)
        self.question_textbox.bind("<KeyRelease>", que_edited)

        question_label = ctk.CTkLabel(master=frame, text="Q"+str(self.id)+":", font=("Agency FB", 50, "bold"), anchor="e")
        question_label.place(relx=0.01, rely=0.09, anchor="w")

        self.marks_entrybox = ctk.CTkEntry(master=frame, width=50, height=50, font=("Sans Serif", 20), justify="center",placeholder_text=self.marks)  # Width decreased
        self.marks_entrybox.place(relx=0.945, rely=0.0873, anchor="center")
        self.marks_entrybox.bind("<KeyRelease>", marks_edited)

        marks_label = ctk.CTkLabel(master=frame, text="Marks:", font=("Agency FB", 39, "bold"), anchor="e")
        marks_label.place(relx=0.845, rely=0.0873, anchor="w")

    def update(self):
        flag = False
        if self.update_que:
            flag = True
            self.que = self.question_textbox.get("1.0", "end-1c")
            self.update_que = False
        if self.update_marks:
            flag = True
            if self.marks_entrybox.get().isdigit():
                self.marks = int(self.marks_entrybox.get())
            self.update_marks = False
        
        if flag:
            self.set()

    def set(self):
        my_con = self.db_connection.cursor()

        if self.retest:
            my_con.execute("Use retest")
        else:
            my_con.execute("Use `{}`".format(self.subject))
        
        my_con.execute("update `{}` set que = %s, marks = %s where id = %s".format(self.exam),(self.que,self.marks,"OEQ"+str(self.id)))

        self.db_connection.commit()
        my_con.close()