import customtkinter as ctk
import ctypes

def new_quiz(course_code : str, exam_type : str, retest : bool):
    quiz = ctk.CTk()
    quiz.title("Quiz Creation")

    quiz.update()  # Ensure window is fully initialized
    hwnd = ctypes.windll.user32.GetForegroundWindow()
    ctypes.windll.user32.ShowWindow(hwnd, 3)  # 3 = SW_MAXIMIZE in Windows API

    # Frame for the top bar (blue color, spans full width)
    top_bar = ctk.CTkFrame(master=quiz, corner_radius=0, fg_color="#2C74B3")  # Blue color
    top_bar.place(relx=0, rely=0, relwidth=1, relheight=0.05)  # Full width, 5% height of the window

    if exam_type == "ClassTest":
        quiz_name = course_code+" Quiz-1"
    else:
        quiz_name = course_code+" "+exam_type
    if retest:
        quiz_name+=" Retest"
    
    # Add the label for the quiz name in the center of the top bar with white font color
    quiz_name_label = ctk.CTkLabel(master=top_bar, text=quiz_name, font=("Agency FB", 28, "bold"), anchor="center", text_color="white")
    quiz_name_label.place(relx=0.5, rely=0.5, anchor="center")  # Centered in the top_bar

    # Frame for the question list
    que_list = ctk.CTkFrame(master=quiz, corner_radius=15, border_width=2, border_color='black')
    que_list.place(relx=0.005, rely=0.06, relwidth=0.18, relheight=0.85)  # Adjusted rely to move frame up

    # New frame beside the que_list frame (taking the rest of the window width)
    side_frame = ctk.CTkFrame(master=quiz, corner_radius=15, border_width=2, border_color='black')
    side_frame.place(relx=0.19, rely=0.06, relwidth=0.805, relheight=0.85)  # Updated width to 0.805

    # Adjusted initial coordinates for button placement (in relative terms within que_list)
    button_relx = 0.07  # Start more towards the left horizontally for first button of each row
    button_rely = 0.09  # Adjusted to be slightly higher (tweaked from 0.08)
    button_count = 1  # Counter to label new buttons
    buttons_per_row = 5  # Maximum buttons in a row

    # Coordinates for Open Ended Questions (OEQ) buttons
    oeq_button_relx = 0.07  # Start horizontally for OEQ button
    oeq_button_rely = 0.82  # Adjust this to place buttons below OEQ label
    oeq_button_count = 1  # Counter to label new OEQ buttons

    # Function to add a new question button (MCQ or OEQ)
    def add_que():
        nonlocal button_relx, button_rely, button_count
        
        # Create a new button with a unique label at the current coordinates
        new_button = ctk.CTkButton(que_list, text=str(button_count), width=40, height=40)
        new_button.place(relx=button_relx, rely=button_rely, relwidth=0.13, relheight=0.05)  # Keep original button dimensions
        
        # Move to the next position with increased horizontal spacing
        if button_count < 45:  # Only shift the add_que_button until the 44th button
            button_relx += 0.18  # Adjusted spacing for better centering

        # Check if we've reached the maximum number of buttons in a row
        if (button_count % buttons_per_row) == 0 and button_count < 45:  # Only shift position if we're below 45
            button_relx = 0.07  # Reset x to start at the left edge for the next row
            button_rely += 0.07  # Increase vertical spacing (adjusted to 0.07)
        
        # Move the '+' button to the new position if button count is less than 45
        if button_count < 45:
            add_que_button.place(relx=button_relx, rely=button_rely, relwidth=0.13, relheight=0.05)  # Keep original button dimensions
        
        # Increment the label count for the new button
        button_count += 1


    # Function to add an Open Ended Question (OEQ) button
    def add_oeq():
        nonlocal oeq_button_relx, oeq_button_rely, oeq_button_count
        
        # Create a new OEQ button at the current coordinates
        new_oeq_button = ctk.CTkButton(que_list, text=str(oeq_button_count), width=40, height=40)
        new_oeq_button.place(relx=oeq_button_relx, rely=oeq_button_rely, relwidth=0.13, relheight=0.05)
        
        # Move to the next position for OEQ buttons
        if oeq_button_count < 10:  # Only shift the add_oeq_button until the 9th button
            oeq_button_relx += 0.18  # Adjusted spacing for OEQ button layout

        # Check if we've reached the maximum number of buttons in a row for OEQ buttons
        if (oeq_button_count % buttons_per_row) == 0 and oeq_button_count < 10:  # Only shift position if we're below 10
            oeq_button_relx = 0.07  # Reset x to start at the left edge for the next row
            oeq_button_rely += 0.07  # Increase vertical spacing (adjusted to 0.07)
        
        # Move the '+' button to the new position if button count is less than 10
        if oeq_button_count < 10:
            add_oeq_button.place(relx=oeq_button_relx, rely=oeq_button_rely, relwidth=0.13, relheight=0.05)

        # Increment the label count for the new OEQ button
        oeq_button_count += 1

        
        # Move the '+' button to the new position
        add_oeq_button.place(relx=oeq_button_relx, rely=oeq_button_rely, relwidth=0.13, relheight=0.05)

    # Create the initial '+' button for MCQs
    add_que_button = ctk.CTkButton(master=que_list, text="+", corner_radius=6, fg_color="green", command=add_que)
    add_que_button.place(relx=button_relx, rely=button_rely, relwidth=0.13, relheight=0.05)  # Keep original button dimensions

    # Create the "Multiple Choice" label above the first row of buttons with updated width
    mcq_label = ctk.CTkLabel(master=que_list, text="Multiple Choice Questions", font=("Agency FB", 28, "bold"), anchor="center")
    mcq_label.place(relx=0.05, rely=0.02, relwidth=0.9, relheight=0.05)  # Updated width to 0.9

    # Label for Open Ended Questions with updated relx to 0.02
    oeq_label = ctk.CTkLabel(master=que_list, text="Open Ended Questions", font=("Agency FB", 28, "bold"), anchor="center")
    oeq_label.place(relx=0.02, rely=0.75, relwidth=0.85, relheight=0.05)  # Updated width to 0.85

    # Create the '+' button for Open Ended Questions below the OEQ label
    add_oeq_button = ctk.CTkButton(master=que_list, text="+", corner_radius=6, fg_color="green", command=add_oeq)
    add_oeq_button.place(relx=0.07, rely=0.82, relwidth=0.13, relheight=0.05)  # Positioned below OEQ label

    prev_button = ctk.CTkButton(master=quiz, text="< Previous", width=100, height=40, corner_radius=6, fg_color="green", font=("Agency FB", 25, 'bold'))
    prev_button.place(relx=0.2, rely=0.93, relwidth=0.1, relheight=0.05)

    next_button = ctk.CTkButton(master=quiz, text="Next >", width=100, height=40, corner_radius=6, fg_color="green", font=("Agency FB", 25, 'bold'))
    next_button.place(relx=0.885, rely=0.93, relwidth=0.1, relheight=0.05)

    schedule_button = ctk.CTkButton(master=quiz, text="Schedule", width=100, height=40, corner_radius=6, fg_color="green", font=("Agency FB", 25, 'bold'))
    schedule_button.place(relx=0.52, rely=0.93, relwidth=0.1, relheight=0.05)

    save_button = ctk.CTkButton(master=quiz, text="Save & Continue Later", width=200, height=40, corner_radius=6, fg_color="green", font=("Agency FB", 25, 'bold'), command=quiz.destroy)
    save_button.place(relx=0.0135, rely=0.93, relwidth=0.16, relheight=0.05)

    quiz.mainloop()
    
def app_win():
    # Create the main application window
    app = ctk.CTk()
    app.title("Course and Assessment Type")
    app.geometry("600x150")  # Same window size as before

    # Function to handle form submission
    def on_submit():
        retest = retest_checkbox.get()
        course_code = course_entry.get()
        exam_type = dropdown.get()
        app.destroy()  # Close the window after submission
        new_quiz(course_code, exam_type, retest)

    # Entry box for course code
    course_entry = ctk.CTkEntry(master=app, placeholder_text="Course Code", font=("Sans Serif", 20), width=200, height=35)
    course_entry.place(relx=0.05, rely=0.2)

    # Dropdown for assessment types (initially blank, no user input allowed)
    dropdown = ctk.CTkComboBox(master=app, values=["MidSem", "EndSem", "ClassTest"], width=200, height=34, font=("Sans Serif", 20), state="readonly")
    dropdown.set("")  # Set initial value to blank
    dropdown.place(relx=0.415, rely=0.2)

    retest_checkbox = ctk.CTkCheckBox(master=app, text="Retest", font=("Sans Serif", 25))
    retest_checkbox.place(relx=0.78, rely=0.22)

    # Submit button (next row)
    submit_button = ctk.CTkButton(master=app, text="Submit", font=("Agency FB", 25, 'bold'), command=on_submit, width=200, height=35)
    submit_button.place(relx=0.29, rely=0.6)  # Centered below entry and dropdown

    # Run the application
    app.mainloop()

win = ctk.CTk()

# Window settings
win.title("MySQL Login")
win.geometry("400x190")  # Set the window size to 400x180

# Label with updated text
label = ctk.CTkLabel(win, text="Enter your MySQL Password", font=("Arial", 20))
label.pack(pady=10)

# Wider entry box with larger font
password_entry = ctk.CTkEntry(win, show="*", width=300, font=("Arial", 18), justify = "center")
password_entry.pack(pady=10)

# Login button with larger font
login_button = ctk.CTkButton(win, text="Login", command=lambda:get_pass(), font=("Arial", 16))
login_button.pack(pady=10)

# Feedback label for connection errors
feedback_label = ctk.CTkLabel(win, text="", font=("Arial", 16))
feedback_label.pack(pady=10)  
password = None
def get_pass():
    global password
    password = password_entry.get()
    win.destroy()
    app_win()

win.mainloop()
