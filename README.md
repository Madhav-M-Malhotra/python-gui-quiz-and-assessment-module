# Python GUI Quiz and Assessment Module (Prototype)

This is a prototype of a Python-based GUI application for quiz and assessment management. The current version includes only the **quiz creation** module — allowing professors to build quizzes with multiple-choice and open-ended questions.

## ✨ Key Highlights

- 🧱 **Clean OOP Architecture**: Modular class-based design with inheritance for different question types.
- 📦 **Efficient Data Structures**:  
  - Doubly Linked List for seamless question navigation  
  - HashSet for fast access and retention of checkbox states  
- 🗃️ **MySQL Database Integration**: Structured storage of quizzes, questions, users, and results.
- 🔐 **Secure Quiz Access**: Passwords are hashed using **SHA-256** before being stored.
- 💡 **User-Friendly GUI**: Built with `CustomTkinter`, featuring dynamic question addition, error handling, and save-progress options.

## 🧰 Technologies Used

- Python 3  
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)  
- MySQL + MySQL Connector for Python  
- `hashlib`, `ctypes` for security & native system interaction  

## 🚀 Getting Started

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Madhav-M-Malhotra/python-gui-quiz-and-assessment-module.git
   ```

2. **Navigate to the folder**:
   ```bash
   cd python-gui-quiz-and-assessment-module
   ```

3. **Install dependencies**:
   ```bash
   pip install customtkinter mysql-connector-python
   ```

4. **Initialize Database**:
   ```bash
   python initialize_db.py
   ```

5. **Run the app**:
   ```bash
   python quiz_creation_prototype.py
   ```

## 🧠 Architecture Overview

### 📦 Object-Oriented Design

- `Quiz` class — Stores metadata like subject, exam type, total marks
- `Que` base class — Defines common attributes for all questions
- `MCQ`, `MultiAns` — Inherit from `Que` and handle single/multi-answer questions
- `QueList` — Implements a **Doubly Linked List** for navigating questions
- `Quiz` object maintains two lists:
  - One for MCQs
  - One for Open-Ended Questions (OEQs)

### 🧮 Data Structures Used

- **Doubly Linked List** for forward/backward traversal of questions.
- **HashSet** for tracking selected answers in multiple-answer MCQs.
- **Database Tables** for:
  - Quiz list and metadata
  - Question papers
  - Section-wise student lists
  - Retests and answer sheets

### 🛡️ Security Measures

- Passwords are hashed using **SHA-256** before being saved to the database.
- GUI has built-in validations and error messages for incomplete or invalid inputs.

## 📸 Screenshots (UI Preview)

Below are visuals from the quiz creation prototype as presented in the project report:

| Quiz Setup Interface | MCQ: Single Correct | MCQ: Multiple Correct |
|---------------------|---------------------|------------------------|
| ![Quiz Setup](assets/quiz_setup.png) | ![Single MCQ](assets/single_mcq.png) | ![Multi MCQ](assets/multi_mcq.png) |

| Open-Ended Question | Password Prompt | MySQL Database View |
|---------------------|------------------|----------------------|
| ![OEQ](assets/oeq.png) | ![Password](assets/pwd.png) | ![Database](assets/dbms.png) |

## 📌 Features Snapshot

- ➕ Add up to **45 MCQs** and **10 OEQs**
- ✍️ Choose between **Single** and **Multiple** correct options
- ⚙️ Grading flexibility: Option-wise or Overall
- 🔁 Navigate with previous/next buttons (DLL-based)
- 💾 "Save & Continue Later" functionality
- 🔑 Password-protected scheduling

## 🗂️ Folder Structure

```
📁 python-gui-quiz-and-assessment-module/
├── assets/                         # Screenshots and resources (images, if any)
├── initialize_db.py                # Script to initialize the MySQL database
├── LICENSE                         # Apache 2.0 License
├── README.md                       # Project documentation (this file)
└── prototype/                      # Main application code
    ├── quiz_creation_prototype.py  # Entry point for the Quiz Creation GUI
    ├── quiz_creation_gui.py        # Quiz Creation win design
    ├── mcq.py                      # MCQ class (single correct)
    ├── multians.py                 # MultiAns class (multiple correct)
    ├── que.py                      # Base Question class for open-ended questions
    ├── quelist.py                  # Doubly Linked List structure for Que navigation
    └── quiz.py                     # Quiz class (holds metadata, MCQ/OEQ lists)
```

## 📃 License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for more details.

---

> 📚 *Developed as a part of the CSC210 - Data Structures & Algorithms course project.*
>  
> 👨‍💻 **Team Members**:  
> Bharvi Vaishnav • Madhav Malhotra • Sachin Yadav
