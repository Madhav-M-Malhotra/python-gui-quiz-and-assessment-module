import customtkinter as ctk
import mysql.connector

class Que:
    def __init__(self, id : int):
        self.id = id
        self.que = None
        self.marks = None
    
    def show(self, frame):        
        # Create the multi-line input Textbox for user to enter a question
        question_textbox = ctk.CTkTextbox(master=frame, width=200, height=200, font=("Sans Serif", 20), border_width=2,placeholder=self.que)  # Increased height
        question_textbox.place(relx=0.455, rely=0.25, relwidth=0.75, relheight=0.4, anchor="center")  # Move slightly to the right

        # Add a label for the question number to the left of the Textbox, aligned with the upper border
        question_label = ctk.CTkLabel(master=frame, text="Q"+str(self.id)+":", font=("Agency FB", 60, "bold"), anchor="e")  # Background color white
        question_label.place(relx=0.03, rely=0.09, anchor="w")  # Moved slightly further down (rely adjusted to 0.09)

        # Create the square-shaped entry box for marks to the right of the question textbox
        marks_entrybox = ctk.CTkEntry(master=frame, width=50, height=50, font=("Sans Serif", 20), justify="center",placeholder=self.marks)  # Width decreased
        marks_entrybox.place(relx=0.945, rely=0.0873, anchor="center")  # Moved slightly to the left and up

        marks_label = ctk.CTkLabel(master=frame, text="Marks:", font=("Agency FB", 39, "bold"), anchor="e")  # Background color white
        marks_label.place(relx=0.845, rely=0.0873, anchor="w")  # Moved slightly further down (rely adjusted to 0.09)

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
        
        my_con.execute("insert into '{}' values({},'{}',NULL,NULL,NULL,NULL,NULL,{},NULL,NULL)".format(exam,self.id,self.que,self.marks))