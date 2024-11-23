import customtkinter as ctk
import mysql.connector
from mcq import MCQ

class MultiAns(MCQ):
    def __init__(self, id: int, db_connection, subject, exam, retest):
        super().__init__(id, db_connection, subject, exam, retest)
        self.grading_type = None

        #flags for checking is the widget was edited
        self.update_grading_type = False
    
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
        def grading_type_edited(*args):
            self.update_grading_type = True

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

        #Grading Type
        self.selected_option = ctk.StringVar()
        option_type = ctk.CTkRadioButton(master=frame, text="Option-wise marking", variable=self.selected_option, value="Option-wise", font=("Agency FB", 25, 'bold'), command=grading_type_edited)
        option_type.place(relx=0.837, rely=0.18)
        overall_type = ctk.CTkRadioButton(master=frame, text="Overall marking", variable=self.selected_option, value="Overall", font=("Agency FB", 25, 'bold'), command=grading_type_edited)
        overall_type.place(relx=0.837, rely=0.25)

        # Create BooleanVars for the checkboxes
        self.checkbox1_var = ctk.BooleanVar()
        self.checkbox2_var = ctk.BooleanVar()
        self.checkbox3_var = ctk.BooleanVar()
        self.checkbox4_var = ctk.BooleanVar()
        
        option1_checkbox = ctk.CTkCheckBox(master=frame, text="a.", variable=self.checkbox1_var, font=("Agency FB", 25, 'bold'), command=ans_edited)
        option1_checkbox.place(relx=0.08, rely=0.5, relwidth=0.3, relheight=0.08)

        self.option1_textbox = ctk.CTkTextbox(master=frame, font=("Sans Serif", 18))
        self.option1_textbox.place(relx=0.12, rely=0.5, relwidth=0.5, relheight=0.08)
        if self.a:
            self.option1_textbox.insert("1.0",self.a)
        self.option1_textbox.bind("<KeyRelease>", option1_edited)

        option2_checkbox = ctk.CTkCheckBox(master=frame, text="b.", variable=self.checkbox2_var, font=("Agency FB", 25, 'bold'), command=ans_edited)
        option2_checkbox.place(relx=0.08, rely=0.62, relwidth=0.3, relheight=0.08)

        self.option2_textbox = ctk.CTkTextbox(master=frame, font=("Sans Serif", 18))
        self.option2_textbox.place(relx=0.12, rely=0.62, relwidth=0.5, relheight=0.08)
        if self.b:
            self.option2_textbox.insert("1.0",self.b)
        self.option2_textbox.bind("<KeyRelease>", option2_edited)

        option3_checkbox = ctk.CTkCheckBox(master=frame, text="c.", variable=self.checkbox3_var, font=("Agency FB", 25, 'bold'), command=ans_edited)
        option3_checkbox.place(relx=0.08, rely=0.74, relwidth=0.3, relheight=0.08)

        self.option3_textbox = ctk.CTkTextbox(master=frame, font=("Sans Serif", 18))
        self.option3_textbox.place(relx=0.12, rely=0.74, relwidth=0.5, relheight=0.08)
        if self.c:
            self.option3_textbox.insert("1.0",self.c)
        self.option3_textbox.bind("<KeyRelease>", option3_edited)

        option4_checkbox = ctk.CTkCheckBox(master=frame, text="d.", variable=self.checkbox4_var, font=("Agency FB", 25, 'bold'), command=ans_edited)
        option4_checkbox.place(relx=0.08, rely=0.86, relwidth=0.3, relheight=0.08)

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
            self.marks = int(self.marks_entrybox.get())
            self.update_marks = False
        
        if self.update_ans:
            flag = True
            self.ans = ''
            if self.checkbox1_var.get():
                self.ans += 'a'
            if self.checkbox2_var.get():
                self.ans += 'b'
            if self.checkbox3_var.get():
                self.ans += 'c'
            if self.checkbox4_var.get():
                self.ans += 'd'
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
        
        if self.update_grading_type:
            flag = True
            self.grading_type = self.selected_option.get()
            self.update_grading_type = False
        
        if flag:
            self.set()

    #overriding set
    def set(self):
        my_con = self.db_connection.cursor()

        if self.retest:
            my_con.execute("Use retest")
        else:
            my_con.execute("Use `{}`".format(self.subject))
        
        my_con.execute("update `{}` set que = %s, a = %s, b = %s, c = %s, d = %s, marks = %s, ans = %s, grading_type = %s where id = %s".format(self.exam),(self.que,self.a,self.b,self.c,self.d,self.marks,self.ans,self.grading_type,"OEQ"+str(self.id)))

        my_con.close()
        