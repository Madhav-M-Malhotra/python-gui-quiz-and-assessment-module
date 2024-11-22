import customtkinter as ctk
from PIL import Image
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

    # Create the multi-line input Textbox for user to enter a question
    question_textbox = ctk.CTkTextbox(master=side_frame, width=200, height=200, font=("Sans Serif", 20), border_width=2)  # Increased height
    question_textbox.place(relx=0.455, rely=0.25, relwidth=0.75, relheight=0.4, anchor="center")  # Move slightly to the right

    # Add a label for the question number to the left of the Textbox, aligned with the upper border
    question_label = ctk.CTkLabel(master=side_frame, text="Q1:", font=("Agency FB", 60, "bold"), anchor="e")  # Background color white
    question_label.place(relx=0.03, rely=0.09, anchor="w")  # Moved slightly further down (rely adjusted to 0.09)

    # Create the square-shaped entry box for marks to the right of the question textbox
    marks_entrybox = ctk.CTkEntry(master=side_frame, width=50, height=50, font=("Sans Serif", 20), justify="center")  # Width decreased
    marks_entrybox.place(relx=0.945, rely=0.0873, anchor="center")  # Moved slightly to the left and up

    marks_label = ctk.CTkLabel(master=side_frame, text="Marks:", font=("Agency FB", 39, "bold"), anchor="e")  # Background color white
    marks_label.place(relx=0.845, rely=0.0873, anchor="w")  # Moved slightly further down (rely adjusted to 0.09)

    #Grading Type
    grading_type = ctk.StringVar()
    option_type = ctk.CTkRadioButton(master=side_frame, text="Option-wise marking", variable=grading_type, value="Option-wise", font=("Agency FB", 25, 'bold'))
    option_type.place(relx=0.837, rely=0.18)
    overall_type = ctk.CTkRadioButton(master=side_frame, text="Overall marking", variable=grading_type, value="Overall", font=("Agency FB", 25, 'bold'))
    overall_type.place(relx=0.837, rely=0.25)

    prev_button = ctk.CTkButton(master=quiz, text="< Previous", width=100, height=40, corner_radius=6, fg_color="green", font=("Agency FB", 25, 'bold'))
    prev_button.place(relx=0.2, rely=0.93, relwidth=0.1, relheight=0.05)

    next_button = ctk.CTkButton(master=quiz, text="Next >", width=100, height=40, corner_radius=6, fg_color="green", font=("Agency FB", 25, 'bold'))
    next_button.place(relx=0.885, rely=0.93, relwidth=0.1, relheight=0.05)

    schedule_button = ctk.CTkButton(master=quiz, text="Schedule", width=100, height=40, corner_radius=6, fg_color="green", font=("Agency FB", 25, 'bold'))
    schedule_button.place(relx=0.52, rely=0.93, relwidth=0.1, relheight=0.05)

    save_button = ctk.CTkButton(master=quiz, text="Save & Continue Later", width=200, height=40, corner_radius=6, fg_color="green", font=("Agency FB", 25, 'bold'), command=quiz.destroy)
    save_button.place(relx=0.0135, rely=0.93, relwidth=0.16, relheight=0.05)

    # Create a StringVar to hold the selected option
    selected_option = ctk.StringVar()
    # Create BooleanVars for the checkboxes
    checkbox3_var = ctk.BooleanVar()
    checkbox4_var = ctk.BooleanVar()

    # Function to handle option selection (optional)
    def on_option_selected():
        print(f"Selected Option: {selected_option.get()}")  # Print the selected option
    # Function to handle checkbox state change
    def on_checkbox_change():
        print(f"Checkbox 3: {checkbox3_var.get()}, Checkbox 4: {checkbox4_var.get()}")

    # Adjusted position for radio buttons and corresponding entry boxes
    option1_button = ctk.CTkRadioButton(master=side_frame, text="a.", variable=selected_option, value="Option a", font=("Agency FB", 25, 'bold'), command=on_option_selected)
    option1_button.place(relx=0.08, rely=0.5, relwidth=0.3, relheight=0.08)

    option1_textbox = ctk.CTkTextbox(master=side_frame, font=("Sans Serif", 18))
    option1_textbox.place(relx=0.12, rely=0.5, relwidth=0.5, relheight=0.08)

    option2_button = ctk.CTkRadioButton(master=side_frame, text="b.", variable=selected_option, value="Option b", font=("Agency FB", 25, 'bold'), command=on_option_selected)
    option2_button.place(relx=0.08, rely=0.62, relwidth=0.3, relheight=0.08)

    option2_textbox = ctk.CTkTextbox(master=side_frame, font=("Sans Serif", 18))
    option2_textbox.place(relx=0.12, rely=0.62, relwidth=0.5, relheight=0.08)

    option3_checkbox = ctk.CTkCheckBox(master=side_frame, text="c.", variable=checkbox3_var, font=("Agency FB", 25, 'bold'), command=on_checkbox_change)
    option3_checkbox.place(relx=0.08, rely=0.74, relwidth=0.3, relheight=0.08)

    option3_textbox = ctk.CTkTextbox(master=side_frame, font=("Sans Serif", 18))
    option3_textbox.place(relx=0.12, rely=0.74, relwidth=0.5, relheight=0.08)

    option4_checkbox = ctk.CTkCheckBox(master=side_frame, text="d.", variable=checkbox4_var, font=("Agency FB", 25, 'bold'), command=on_checkbox_change)
    option4_checkbox.place(relx=0.08, rely=0.86, relwidth=0.3, relheight=0.08)

    option4_textbox = ctk.CTkTextbox(master=side_frame, font=("Sans Serif", 18))
    option4_textbox.place(relx=0.12, rely=0.86, relwidth=0.5, relheight=0.08)


    quiz.mainloop()
    
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
