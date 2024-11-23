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

        my_con = db_connection.cursor()

        if retest:
            my_con.execute("Use retest")
        else:
            my_con.execute("Use '{}'".format(subject))
    
        my_con.execute("insert into '{}'(id) values({})".format(exam,"MCQ"+str(self.id)))

        my_con.close()
    
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

        # Create a StringVar to hold the selected option
        selected_option = ctk.StringVar()
        # Function to handle option selection
        def on_option_selected():
            print(f"Selected Option: {selected_option.get()}")  # Print the selected option

        option1_button = ctk.CTkRadioButton(master=frame, text="a.", variable=selected_option, value="Option a", font=("Agency FB", 25, 'bold'), command=on_option_selected)
        option1_button.place(relx=0.08, rely=0.5, relwidth=0.3, relheight=0.08)

        option1_textbox = ctk.CTkTextbox(master=frame, font=("Sans Serif", 18))
        option1_textbox.place(relx=0.12, rely=0.5, relwidth=0.5, relheight=0.08)
        if self.a:
            option1_textbox.insert("1.0",self.a)

        option2_button = ctk.CTkRadioButton(master=frame, text="b.", variable=selected_option, value="Option b", font=("Agency FB", 25, 'bold'), command=on_option_selected)
        option2_button.place(relx=0.08, rely=0.62, relwidth=0.3, relheight=0.08)

        option2_textbox = ctk.CTkTextbox(master=frame, font=("Sans Serif", 18))
        option2_textbox.place(relx=0.12, rely=0.62, relwidth=0.5, relheight=0.08)
        if self.b:
            option2_textbox.insert("1.0",self.b)

        option3_button = ctk.CTkRadioButton(master=frame, text="c.", variable=selected_option, value="Option c", font=("Agency FB", 25, 'bold'), command=on_option_selected)
        option3_button.place(relx=0.08, rely=0.74, relwidth=0.3, relheight=0.08)

        option3_textbox = ctk.CTkTextbox(master=frame, font=("Sans Serif", 18))
        option3_textbox.place(relx=0.12, rely=0.74, relwidth=0.5, relheight=0.08)
        if self.c:
            option3_textbox.insert("1.0",self.c)

        option4_button = ctk.CTkRadioButton(master=frame, text="d.", variable=selected_option, value="Option d", font=("Agency FB", 25, 'bold'), command=on_option_selected)
        option4_button.place(relx=0.08, rely=0.86, relwidth=0.3, relheight=0.08)

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
        
        my_con.execute("insert into '{}' values({},'{}',NULL,'{}','{}','{}','{}',{},'{}',NULL)".format(exam,self.id,self.que,self.a,self.b,self.c,self.d,self.marks,self.ans))
        