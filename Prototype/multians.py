import customtkinter as ctk
import mysql.connector
from mcq import MCQ

class MultiAns(MCQ):
    def __init__(self, id: int, db_connection, subject, exam, retest):
        super().__init__(id, db_connection, subject, exam, retest)
        self.grading_type = None
    
    #overridng show
    def show(self, frame):
        # Create the multi-line input Textbox for user to enter a question
        question_textbox = ctk.CTkTextbox(master=frame, width=200, height=200, font=("Sans Serif", 20), border_width=2)  # Increased height
        question_textbox.place(relx=0.455, rely=0.25, relwidth=0.75, relheight=0.4, anchor="center")  # Move slightly to the right
        if self.que:
            question_textbox.insert("1.0",self.que)

        # Add a label for the question number to the left of the Textbox, aligned with the upper border
        question_label = ctk.CTkLabel(master=frame, text="Q"+str(self.id)+":", font=("Agency FB", 50, "bold"), anchor="e")  # Background color white
        question_label.place(relx=0.01, rely=0.09, anchor="w")  # Moved slightly further down (rely adjusted to 0.09)

        # Create the square-shaped entry box for marks to the right of the question textbox
        marks_entrybox = ctk.CTkEntry(master=frame, width=50, height=50, font=("Sans Serif", 20), justify="center",placeholder_text=self.marks)  # Width decreased
        marks_entrybox.place(relx=0.945, rely=0.0873, anchor="center")  # Moved slightly to the left and up

        marks_label = ctk.CTkLabel(master=frame, text="Marks:", font=("Agency FB", 39, "bold"), anchor="e")  # Background color white
        marks_label.place(relx=0.845, rely=0.0873, anchor="w")  # Moved slightly further down (rely adjusted to 0.09)

        #Grading Type
        grading_type = ctk.StringVar()
        option_type = ctk.CTkRadioButton(master=frame, text="Option-wise marking", variable=grading_type, value="Option-wise", font=("Agency FB", 25, 'bold'))
        option_type.place(relx=0.837, rely=0.18)
        overall_type = ctk.CTkRadioButton(master=frame, text="Overall marking", variable=grading_type, value="Overall", font=("Agency FB", 25, 'bold'))
        overall_type.place(relx=0.837, rely=0.25)

        # Create BooleanVars for the checkboxes
        checkbox1_var = ctk.BooleanVar()
        checkbox2_var = ctk.BooleanVar()
        checkbox3_var = ctk.BooleanVar()
        checkbox4_var = ctk.BooleanVar()
        # Function to handle checkbox state change
        def on_checkbox_change():
            print(f"Checkbox 1: {checkbox1_var.get()}, Checkbox 2: {checkbox2_var.get()}, Checkbox 3: {checkbox3_var.get()}, Checkbox 4: {checkbox4_var.get()}")

        option1_checkbox = ctk.CTkCheckBox(master=frame, text="a.", variable=checkbox1_var, font=("Agency FB", 25, 'bold'), command=on_checkbox_change)
        option1_checkbox.place(relx=0.08, rely=0.5, relwidth=0.3, relheight=0.08)

        option1_textbox = ctk.CTkTextbox(master=frame, font=("Sans Serif", 18))
        option1_textbox.place(relx=0.12, rely=0.5, relwidth=0.5, relheight=0.08)
        if self.a:
            option1_textbox.insert("1.0",self.a)

        option2_checkbox = ctk.CTkCheckBox(master=frame, text="b.", variable=checkbox2_var, font=("Agency FB", 25, 'bold'), command=on_checkbox_change)
        option2_checkbox.place(relx=0.08, rely=0.62, relwidth=0.3, relheight=0.08)

        option2_textbox = ctk.CTkTextbox(master=frame, font=("Sans Serif", 18))
        option2_textbox.place(relx=0.12, rely=0.62, relwidth=0.5, relheight=0.08)
        if self.b:
            option2_textbox.insert("1.0",self.b)

        option3_checkbox = ctk.CTkCheckBox(master=frame, text="c.", variable=checkbox3_var, font=("Agency FB", 25, 'bold'), command=on_checkbox_change)
        option3_checkbox.place(relx=0.08, rely=0.74, relwidth=0.3, relheight=0.08)

        option3_textbox = ctk.CTkTextbox(master=frame, font=("Sans Serif", 18))
        option3_textbox.place(relx=0.12, rely=0.74, relwidth=0.5, relheight=0.08)
        if self.c:
            option3_textbox.insert("1.0",self.c)

        option4_checkbox = ctk.CTkCheckBox(master=frame, text="d.", variable=checkbox4_var, font=("Agency FB", 25, 'bold'), command=on_checkbox_change)
        option4_checkbox.place(relx=0.08, rely=0.86, relwidth=0.3, relheight=0.08)

        option4_textbox = ctk.CTkTextbox(master=frame, font=("Sans Serif", 18))
        option4_textbox.place(relx=0.12, rely=0.86, relwidth=0.5, relheight=0.08)
        if self.d:
            option4_textbox.insert("1.0",self.d)

    #overriding set
    def set(self, password, subject, exam, retest):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  # Replace with actual username
            password=password
        )
        my_con = connection.cursor()

        if retest:
            my_con.execute("Use retest")
        else:
            my_con.execute("Use '{}'".format(subject))
        
        my_con.execute("insert into '{}' values({},'{}',NULL,'{}','{}','{}','{}',{},'{}','{}')".format(exam,self.id,self.que,self.a,self.b,self.c,self.d,self.marks,self.ans,self.grading_type))
        