import customtkinter as ctk
import mysql.connector
import ctypes
from quiz import QueList,Quiz
from que import Que
from multians import MCQ,MultiAns

def new_quiz(course_code : str, exam_type : str, retest : bool):
    #settingup mysql connection
    connection = mysql.connector.connect(
            host="localhost",
            user="root",#Replace with your username
            password=password
        )

    quiz_win = ctk.CTk()
    quiz_win.title("Quiz Creation")

    quiz_win.update()#Ensure window is fully initialized
    hwnd = ctypes.windll.user32.GetForegroundWindow()
    ctypes.windll.user32.ShowWindow(hwnd, 3)#3 = SW_MAXIMIZE in Windows API

    #Frame for the top bar (blue color, spans full width)
    top_bar = ctk.CTkFrame(master=quiz_win, corner_radius=0, fg_color="#2C74B3")
    top_bar.place(relx=0, rely=0, relwidth=1, relheight=0.05)

    if exam_type == "ClassTest":
        exam_type = "Quiz_1"
        quiz_name = course_code+" Quiz 1"
    else:
        quiz_name = course_code+" "+exam_type
    if retest:
        quiz_name+=" Retest"
    
    quiz = Quiz(connection,course_code,exam_type,retest)
    current_que = None

    quiz_name_label = ctk.CTkLabel(master=top_bar, text=quiz_name, font=("Agency FB", 28, "bold"), anchor="center", text_color="white")
    quiz_name_label.place(relx=0.5, rely=0.5, anchor="center")  # Centered in the top_bar

    #Frame for the question list
    que_list = ctk.CTkFrame(master=quiz_win, corner_radius=15, border_width=2, border_color='black')
    que_list.place(relx=0.005, rely=0.06, relwidth=0.18, relheight=0.85)

    #Frame for the questions
    side_frame = ctk.CTkFrame(master=quiz_win, corner_radius=15, border_width=2, border_color='black')
    side_frame.place(relx=0.19, rely=0.06, relwidth=0.805, relheight=0.85)

    #Adjusted initial coordinates for button placement (in relative terms within que_list)
    button_relx = 0.07
    button_rely = 0.09
    button_count = 1#Counter to label new buttons
    buttons_per_row = 5#Maximum buttons in a row
    on_mcq_selection = False

    #Coordinates for Open Ended Questions (OEQ) buttons
    oeq_button_relx = 0.07
    oeq_button_rely = 0.82
    oeq_button_count = 1#Counter to label new OEQ buttons

    #function to clear the question from the frame
    def clear_frame():
        for widget in side_frame.winfo_children():
            widget.destroy()

    #Function to add a new MCQ
    def add_mcq():        
        nonlocal button_relx, button_rely, button_count, current_que, on_mcq_selection
        
        if current_que:
            current_que.que.update()
            clear_frame()
        
        current_que = quiz.mcq.tail
        if button_count == quiz.mcq.length+1:
            #Create a new button with a unique label at the current coordinates
            new_button = ctk.CTkButton(que_list, text=str(button_count), width=40, height=40)
            new_button.place(relx=button_relx, rely=button_rely, relwidth=0.13, relheight=0.05)
            
            #shift the add_mcq_button until the 44th button
            if button_count < 45:
                button_relx += 0.18

            #Check if we've reached the maximum number of buttons in a row
            if (button_count % buttons_per_row) == 0 and button_count < 45:#Only shift position if we're below 45
                button_relx = 0.07#Reset x to start at the left edge for the next row
                button_rely += 0.07#Increase y
            
            #Move the '+' button to the new position if button count is less than 45
            if button_count < 45:
                add_mcq_button.place(relx=button_relx, rely=button_rely, relwidth=0.13, relheight=0.05)
            
            #Increment the button count
            button_count += 1

        def new_mcq():
            nonlocal current_que, on_mcq_selection
            clear_frame()
            quiz.mcq.add(MCQ(button_count-1,connection,course_code,exam_type,retest))
            quiz.mcq.tail.que.show(side_frame)
            current_que = quiz.mcq.tail
            on_mcq_selection = False
            
        def new_multians():
            nonlocal current_que, on_mcq_selection
            clear_frame()
            quiz.mcq.add(MultiAns(button_count-1,connection,course_code,exam_type,retest))
            quiz.mcq.tail.que.show(side_frame)
            current_que = quiz.mcq.tail
            on_mcq_selection = False

        #choosing question type
        single_answer = ctk.CTkButton(side_frame, text="Single-Answer", width=250, height=40, corner_radius=6, font=("Agency FB", 35, 'bold'), command=new_mcq)
        single_answer.place(relx=0.475, rely=0.38, anchor="center")

        or_label = ctk.CTkLabel(side_frame, text="OR", font=("Agency FB", 25, 'bold'))
        or_label.place(relx=0.48, rely=0.475, anchor="center")

        multi_answer = ctk.CTkButton(side_frame, text="Multi-Answer", width=250, height=40, corner_radius=6, font=("Agency FB", 35, 'bold'), command=new_multians)
        multi_answer.place(relx=0.475, rely=0.58, anchor="center")

        next_button.configure(state="disabled")
        if current_que:
                prev_button.configure(state="normal")
        on_mcq_selection = True

    #Function to add a new OEQ
    def add_oeq():
        nonlocal oeq_button_relx, oeq_button_rely, oeq_button_count, current_que, on_mcq_selection
        
        if current_que:
            current_que.que.update()
        clear_frame()

        #Create a new OEQ button at the current coordinates
        new_oeq_button = ctk.CTkButton(que_list, text=str(oeq_button_count), width=40, height=40)
        new_oeq_button.place(relx=oeq_button_relx, rely=oeq_button_rely, relwidth=0.13, relheight=0.05)
        
        #shift the add_oeq_button until the 9th button
        if oeq_button_count < 10:
            oeq_button_relx += 0.18

        #Check if we've reached the maximum number of buttons in a row for OEQ buttons
        if (oeq_button_count % buttons_per_row) == 0 and oeq_button_count < 10:#Only shift position if we're below 10
            oeq_button_relx = 0.07#Reset x to start at the left edge for the next row
            oeq_button_rely += 0.07#Increase y
        
        #Move the '+' button to the new position if button count is less than 10
        if oeq_button_count < 10:
            add_oeq_button.place(relx=oeq_button_relx, rely=oeq_button_rely, relwidth=0.13, relheight=0.05)

        #adding question
        quiz.oe.add(Que(oeq_button_count,connection,course_code,exam_type,retest))
        quiz.oe.tail.que.show(side_frame)
        current_que = quiz.oe.tail
        on_mcq_selection = False

        next_button.configure(state="disabled")
        if current_que.prev:
            prev_button.configure(state="normal")
        else:
            prev_button.configure(state="disabled")

        #Increment oeq button count
        oeq_button_count += 1

    def goto_mcqhead():
        nonlocal current_que
        if quiz.mcq.head:
            if current_que != quiz.mcq.head:
                current_que.que.update()
                clear_frame()
                current_que = quiz.mcq.head
                current_que.que.show(side_frame)
                prev_button.configure(state="disabled")
                if button_count>2:
                    next_button.configure(state="normal")
        elif button_count == 2:
            add_mcq()

    def goto_oehead():
        nonlocal current_que
        if quiz.oe.head:
            if current_que != quiz.oe.head:
                if current_que:
                    current_que.que.update()
                clear_frame()
                current_que = quiz.oe.head
                current_que.que.show(side_frame)
                prev_button.configure(state="disabled")
                if current_que != quiz.oe.tail:
                    next_button.configure(state="normal")

    #Create the initial '+' button for MCQs
    add_mcq_button = ctk.CTkButton(master=que_list, text="+", corner_radius=6, fg_color="green", command=add_mcq)
    add_mcq_button.place(relx=button_relx, rely=button_rely, relwidth=0.13, relheight=0.05)

    mcq_label = ctk.CTkLabel(master=que_list, text="Multiple Choice Questions", font=("Agency FB", 28, "bold"), anchor="center")
    mcq_label.place(relx=0.05, rely=0.02, relwidth=0.9, relheight=0.05)
    mcq_label.bind('<Button>',lambda e:goto_mcqhead())

    oeq_label = ctk.CTkLabel(master=que_list, text="Open Ended Questions", font=("Agency FB", 28, "bold"), anchor="center")
    oeq_label.place(relx=0.02, rely=0.75, relwidth=0.85, relheight=0.05)
    oeq_label.bind('<Button>',lambda e:goto_oehead())

    #Create the '+' button for Open Ended Questions below the OEQ label
    add_oeq_button = ctk.CTkButton(master=que_list, text="+", corner_radius=6, fg_color="green", command=add_oeq)
    add_oeq_button.place(relx=0.07, rely=0.82, relwidth=0.13, relheight=0.05)

    def prev():
        nonlocal current_que, on_mcq_selection

        current_que.que.update()
        clear_frame()
    
        if not on_mcq_selection:
            current_que = current_que.prev
        current_que.que.show(side_frame)
        on_mcq_selection = False

        next_button.configure(state="normal")
        if current_que.prev:
            prev_button.configure(state="normal")
        else:
            prev_button.configure(state="disabled")
    
    def next():
        nonlocal current_que

        current_que.que.update()
        clear_frame()

        if current_que == quiz.mcq.tail:
            add_mcq()
            return
        current_que = current_que.next
        current_que.que.show(side_frame)

        prev_button.configure(state="normal")
        if (current_que != quiz.oe.tail) and ((current_que != quiz.mcq.tail) or (button_count == quiz.mcq.length+2)):
            next_button.configure(state="normal")
        else:
            next_button.configure(state="disabled")

    prev_button = ctk.CTkButton(master=quiz_win, text="< Previous", width=100, height=40, corner_radius=6, fg_color="green", font=("Agency FB", 25, 'bold'), state="disabled", command=prev)
    prev_button.place(relx=0.2, rely=0.93, relwidth=0.1, relheight=0.05)

    next_button = ctk.CTkButton(master=quiz_win, text="Next >", width=100, height=40, corner_radius=6, fg_color="green", font=("Agency FB", 25, 'bold'), state="disabled", command=next)
    next_button.place(relx=0.885, rely=0.93, relwidth=0.1, relheight=0.05)

    def schedule():
        nonlocal exam_type, course_code, current_que

        if current_que:
            current_que.que.update()

        def error_popup(que_list,que):
            # Create a pop-up window
            popup = ctk.CTkToplevel(quiz_win)
            popup.geometry("590x150")  # Set the size of the pop-up
            popup.title("Error")
            popup.resizable(False, False)  # Prevent resizing
            
            # Center the pop-up on the screen
            x = (quiz_win.winfo_x() + quiz_win.winfo_width() // 2 - popup.winfo_width() // 2)
            y = (quiz_win.winfo_y() + quiz_win.winfo_height() // 2 - popup.winfo_height() // 2)
            popup.geometry(f"+{x}+{y}")
            
            if que == 0:
                message = "*ERROR : Quiz doesn't have any questions*"
            else:
                message = "*ERROR : Incomplete data in "+que_list+" question "+str(que)+"*"
            # Add an error message label
            error_label = ctk.CTkLabel(popup, text=message, text_color="#D32F2F", font=("Sans Serif", 25, "bold"))
            error_label.pack(pady=20)
            
            # Add an "OK" button
            def close_popup():
                popup.destroy()  # Destroy the pop-up

            ok_button = ctk.CTkButton(popup, text="OK", font=("Agency FB", 25, 'bold'), command=close_popup)
            ok_button.pack(pady=10)

            popup.grab_set()
            # Prevent interaction with the main window while the pop-up is open
            popup.protocol("WM_DELETE_WINDOW", lambda: None)  # Disable close button on the pop-up

        curr_mcq = quiz.mcq.head
        curr_oe = quiz.oe.head
        if (curr_mcq is None) and (curr_oe is None):
            error_popup("",0)
            return
        while curr_mcq and curr_oe:
            if curr_mcq.que.ready_for_scheduling:
                curr_mcq = curr_mcq.next
            else:
                error_popup("MCQ",curr_mcq.que.id)
                return
            if curr_oe.que.ready_for_scheduling:
                curr_oe = curr_oe.next
            else:
                error_popup("OEQ",curr_oe.que.id)
                return
        while curr_mcq:
            if curr_mcq.que.ready_for_scheduling:
                curr_mcq = curr_mcq.next
            else:
                error_popup("MCQ",curr_mcq.que.id)
                return
        while curr_oe:
            if curr_oe.que.ready_for_scheduling:
                curr_oe = curr_oe.next
            else:
                error_popup("OEQ",curr_oe.que.id)
                return

    schedule_button = ctk.CTkButton(master=quiz_win, text="Schedule", width=100, height=40, corner_radius=6, fg_color="green", font=("Agency FB", 25, 'bold'), command=schedule)
    schedule_button.place(relx=0.52, rely=0.93, relwidth=0.1, relheight=0.05)

    def save():
        if current_que:
            current_que.que.update()
        quiz_win.destroy()

    save_button = ctk.CTkButton(master=quiz_win, text="Save & Continue Later", width=200, height=40, corner_radius=6, fg_color="green", font=("Agency FB", 25, 'bold'), command=save)
    save_button.place(relx=0.0135, rely=0.93, relwidth=0.16, relheight=0.05)

    quiz_win.mainloop()
    
def app_win():
    app = ctk.CTk()
    app.title("Course and Assessment Type")
    app.geometry("600x150")

    #Function to handle form submission
    def on_submit():
        retest = retest_checkbox.get()
        course_code = course_entry.get()
        exam_type = dropdown.get()
        app.destroy()#Close the window after submission
        new_quiz(course_code, exam_type, retest)

    #Entry box for course code
    course_entry = ctk.CTkEntry(master=app, placeholder_text="Course Code", font=("Sans Serif", 20), width=200, height=35)
    course_entry.place(relx=0.05, rely=0.2)

    #Dropdown for assessment types
    dropdown = ctk.CTkComboBox(master=app, values=["MidSem", "EndSem", "ClassTest"], width=200, height=34, font=("Sans Serif", 20), state="readonly")
    dropdown.set("")#Set initial value to blank
    dropdown.place(relx=0.415, rely=0.2)

    retest_checkbox = ctk.CTkCheckBox(master=app, text="Retest", font=("Sans Serif", 25))
    retest_checkbox.place(relx=0.78, rely=0.22)

    submit_button = ctk.CTkButton(master=app, text="Submit", font=("Agency FB", 25, 'bold'), command=on_submit, width=200, height=35)
    submit_button.place(relx=0.29, rely=0.6)

    app.mainloop()

win = ctk.CTk()

win.title("MySQL Login")
win.geometry("400x190")

label = ctk.CTkLabel(win, text="Enter your MySQL Password", font=("Arial", 20))
label.pack(pady=10)

password_entry = ctk.CTkEntry(win, show="*", width=300, font=("Arial", 18), justify = "center")
password_entry.pack(pady=10)

login_button = ctk.CTkButton(win, text="Login", command=lambda:get_pass(), font=("Arial", 16))
login_button.pack(pady=10)

password = None
def get_pass():
    global password
    password = password_entry.get()
    win.destroy()
    app_win()

win.mainloop()
