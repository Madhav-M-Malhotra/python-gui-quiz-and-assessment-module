import customtkinter as ctk
import mysql.connector
from que import Que

class MCQ(Que):
    def __init__(self, id: int, db_connection, subject, exam, retest):
        super().__init__(id, db_connection, subject, exam, retest)
        self.a = None
        self.b = None
        self.c = None
        self.d = None
        self.ans = None

        #flags for checking is the widget was edited
        self.update_ans = False
        self.update_option1 = False
        self.update_option2 = False
        self.update_option3 = False
        self.update_option4 = False

        my_con = db_connection.cursor()

        if retest:
            my_con.execute("Use retest")
        else:
            my_con.execute("Use '{}'".format(subject))
    
        my_con.execute("insert into '{}'(id) values({})".format(exam,"MCQ"+str(self.id)))

        my_con.close()
    
    #overridng show
    def show(self, frame):
        #functions to set flag True
        def que_edited():
            self.update_que = True
        def marks_edited():
            self.update_marks = True
        def ans_edited():
            self.update_ans = True
        def option1_edited():
            self.update_option1 = True
        def option2_edited():
            self.update_option2 = True
        def option3_edited():
            self.update_option3 = True
        def option4_edited():
            self.update_option4 = True

        # Create the multi-line input Textbox for user to enter a question
        question_textbox = ctk.CTkTextbox(master=frame, width=200, height=200, font=("Sans Serif", 20), border_width=2)  # Increased height
        question_textbox.place(relx=0.455, rely=0.25, relwidth=0.75, relheight=0.4, anchor="center")  # Move slightly to the right
        if self.que:
            question_textbox.insert("1.0",self.que)
        question_textbox.bind("<KeyRelease>", que_edited)

        # Add a label for the question number to the left of the Textbox, aligned with the upper border
        question_label = ctk.CTkLabel(master=frame, text="Q"+str(self.id)+":", font=("Agency FB", 50, "bold"), anchor="e")  # Background color white
        question_label.place(relx=0.01, rely=0.09, anchor="w")  # Moved slightly further down (rely adjusted to 0.09)

        # Create the square-shaped entry box for marks to the right of the question textbox
        marks_entrybox = ctk.CTkEntry(master=frame, width=50, height=50, font=("Sans Serif", 20), justify="center",placeholder_text=self.marks)  # Width decreased
        marks_entrybox.place(relx=0.945, rely=0.0873, anchor="center")  # Moved slightly to the left and up
        marks_entrybox.bind("<KeyRelease>", marks_edited)

        marks_label = ctk.CTkLabel(master=frame, text="Marks:", font=("Agency FB", 39, "bold"), anchor="e")  # Background color white
        marks_label.place(relx=0.845, rely=0.0873, anchor="w")  # Moved slightly further down (rely adjusted to 0.09)

        # Create a StringVar to hold the selected option
        selected_option = ctk.StringVar()

        option1_button = ctk.CTkRadioButton(master=frame, text="a.", variable=selected_option, value="Option a", font=("Agency FB", 25, 'bold'), command=ans_edited)
        option1_button.place(relx=0.08, rely=0.5, relwidth=0.3, relheight=0.08)

        option1_textbox = ctk.CTkTextbox(master=frame, font=("Sans Serif", 18))
        option1_textbox.place(relx=0.12, rely=0.5, relwidth=0.5, relheight=0.08)
        if self.a:
            option1_textbox.insert("1.0",self.a)
        option1_textbox.bind("<KeyRelease>", option1_edited)

        option2_button = ctk.CTkRadioButton(master=frame, text="b.", variable=selected_option, value="Option b", font=("Agency FB", 25, 'bold'), command=ans_edited)
        option2_button.place(relx=0.08, rely=0.62, relwidth=0.3, relheight=0.08)

        option2_textbox = ctk.CTkTextbox(master=frame, font=("Sans Serif", 18))
        option2_textbox.place(relx=0.12, rely=0.62, relwidth=0.5, relheight=0.08)
        if self.b:
            option2_textbox.insert("1.0",self.b)
        option2_textbox.bind("<KeyRelease>", option2_edited)

        option3_button = ctk.CTkRadioButton(master=frame, text="c.", variable=selected_option, value="Option c", font=("Agency FB", 25, 'bold'), command=ans_edited)
        option3_button.place(relx=0.08, rely=0.74, relwidth=0.3, relheight=0.08)

        option3_textbox = ctk.CTkTextbox(master=frame, font=("Sans Serif", 18))
        option3_textbox.place(relx=0.12, rely=0.74, relwidth=0.5, relheight=0.08)
        if self.c:
            option3_textbox.insert("1.0",self.c)
        option3_textbox.bind("<KeyRelease>", option3_edited)

        option4_button = ctk.CTkRadioButton(master=frame, text="d.", variable=selected_option, value="Option d", font=("Agency FB", 25, 'bold'), command=ans_edited)
        option4_button.place(relx=0.08, rely=0.86, relwidth=0.3, relheight=0.08)

        option4_textbox = ctk.CTkTextbox(master=frame, font=("Sans Serif", 18))
        option4_textbox.place(relx=0.12, rely=0.86, relwidth=0.5, relheight=0.08)
        if self.d:
            option4_textbox.insert("1.0",self.d)
        option4_textbox.bind("<KeyRelease>", option4_edited)

    #overriding set
    def set(self):
        my_con = self.db_connection.cursor()

        if self.retest:
            my_con.execute("Use retest")
        else:
            my_con.execute("Use '{}'".format(self.subject))
        
        my_con.execute("update '{}' set que = '{}', a = '{}', b = '{}', c = '{}', d = '{}', marks = {}, ans = '{}' where id = '{}'".format(self.exam,self.que,self.a,self.b,self.c,self.d,self.marks,self.ans,"OEQ"+str(self.id)))

        my_con.close()
        