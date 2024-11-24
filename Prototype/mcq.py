import customtkinter as ctk
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
            self.exam = subject+"_"+exam
            my_con.execute("Use retest")
        else:
            my_con.execute("Use `{}`".format(subject))
    
        my_con.execute("insert into `{}`(id) values('{}')".format(exam,"MCQ"+str(self.id)))

        my_con.close()
    
    #overridng show
    def show(self, frame):
        #functions to set flag True
        def que_edited(*args):
            self.update_que = True
        def marks_edited(*args):
            self.update_marks = True
        def ans_edited(*args):
            self.update_ans = True
        def option1_edited(*args):
            self.update_option1 = True
        def option2_edited(*args):
            self.update_option2 = True
        def option3_edited(*args):
            self.update_option3 = True
        def option4_edited(*args):
            self.update_option4 = True

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

        # Create a StringVar to hold the selected option
        self.selected_option = ctk.StringVar()
        if self.ans:
            self.selected_option.set(self.ans)

        option1_button = ctk.CTkRadioButton(master=frame, text="a.", variable=self.selected_option, value="a", font=("Agency FB", 25, 'bold'), command=ans_edited)
        option1_button.place(relx=0.08, rely=0.5, relwidth=0.3, relheight=0.08)

        self.option1_textbox = ctk.CTkTextbox(master=frame, font=("Sans Serif", 18))
        self.option1_textbox.place(relx=0.12, rely=0.5, relwidth=0.5, relheight=0.08)
        if self.a:
            self.option1_textbox.insert("1.0",self.a)
        self.option1_textbox.bind("<KeyRelease>", option1_edited)

        option2_button = ctk.CTkRadioButton(master=frame, text="b.", variable=self.selected_option, value="b", font=("Agency FB", 25, 'bold'), command=ans_edited)
        option2_button.place(relx=0.08, rely=0.62, relwidth=0.3, relheight=0.08)

        self.option2_textbox = ctk.CTkTextbox(master=frame, font=("Sans Serif", 18))
        self.option2_textbox.place(relx=0.12, rely=0.62, relwidth=0.5, relheight=0.08)
        if self.b:
            self.option2_textbox.insert("1.0",self.b)
        self.option2_textbox.bind("<KeyRelease>", option2_edited)

        option3_button = ctk.CTkRadioButton(master=frame, text="c.", variable=self.selected_option, value="c", font=("Agency FB", 25, 'bold'), command=ans_edited)
        option3_button.place(relx=0.08, rely=0.74, relwidth=0.3, relheight=0.08)

        self.option3_textbox = ctk.CTkTextbox(master=frame, font=("Sans Serif", 18))
        self.option3_textbox.place(relx=0.12, rely=0.74, relwidth=0.5, relheight=0.08)
        if self.c:
            self.option3_textbox.insert("1.0",self.c)
        self.option3_textbox.bind("<KeyRelease>", option3_edited)

        option4_button = ctk.CTkRadioButton(master=frame, text="d.", variable=self.selected_option, value="d", font=("Agency FB", 25, 'bold'), command=ans_edited)
        option4_button.place(relx=0.08, rely=0.86, relwidth=0.3, relheight=0.08)

        self.option4_textbox = ctk.CTkTextbox(master=frame, font=("Sans Serif", 18))
        self.option4_textbox.place(relx=0.12, rely=0.86, relwidth=0.5, relheight=0.08)
        if self.d:
            self.option4_textbox.insert("1.0",self.d)
        self.option4_textbox.bind("<KeyRelease>", option4_edited)

    #overriding update
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
        
        if self.update_ans:
            flag = True
            self.ans = self.selected_option.get()
            self.update_ans = False
        
        if self.update_option1:
            flag = True
            self.a = self.option1_textbox.get("1.0", "end-1c")
            self.update_option1 = False
        if self.update_option2:
            flag = True
            self.b = self.option2_textbox.get("1.0", "end-1c")
            self.update_option2 = False
        if self.update_option3:
            flag = True
            self.c = self.option3_textbox.get("1.0", "end-1c")
            self.update_option3 = False
        if self.update_option4:
            flag = True
            self.d = self.option4_textbox.get("1.0", "end-1c")
            self.update_option4 = False
        
        if flag:
            self.set()

    #overriding set
    def set(self):
        my_con = self.db_connection.cursor()

        if self.retest:
            my_con.execute("Use retest")
        else:
            my_con.execute("Use `{}`".format(self.subject))
        
        my_con.execute("update `{}` set que = %s, a = %s, b = %s, c = %s, d = %s, marks = %s, ans = %s where id = %s".format(self.exam),(self.que,self.a,self.b,self.c,self.d,self.marks,self.ans,"OEQ"+str(self.id)))

        my_con.close()
        