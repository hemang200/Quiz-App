import os
import random

# File paths
users_file = os.path.join(os.getcwd(), "usersdata.txt")
results_file = os.path.join(os.getcwd(), "usersresults.txt")

# Quiz questions
quizzes = {
    "DSA": [
        {"question": "What is the time complexity of binary search?", "options": ["O(n)", "O(log n)", "O(n^2)"], "answer": "O(log n)"},
        {"question": "Which data structure is used in BFS?", "options": ["Stack", "Queue", "Tree"], "answer": "Queue"},
        {"question": "What is the worst-case time complexity of quicksort?", "options": ["O(n^2)", "O(n log n)", "O(n)"], "answer": "O(n^2)"},
        {"question": "Which of the following is not a linear data structure?", "options": ["Array", "Tree", "Linked List"], "answer": "Tree"},
        {"question": "Which data structure allows LIFO?", "options": ["Queue", "Stack", "Array"], "answer": "Stack"},
        {"question": "Which data structure is used for recursion?", "options": ["Queue", "Stack", "Tree"], "answer": "Stack"},
        {"question": "What is the space complexity of a linked list?", "options": ["O(1)", "O(n)", "O(n^2)"], "answer": "O(n)"},
        {"question": "Which algorithm is used in finding the shortest path in graphs?", "options": ["Dijkstra's", "Kruskal's", "Prim's"], "answer": "Dijkstra's"},
        {"question": "Which data structure uses key-value pairs?", "options": ["HashMap", "Stack", "Queue"], "answer": "HashMap"},
        {"question": "What is the time complexity of merging two sorted arrays?", "options": ["O(m+n)", "O(log n)", "O(n^2)"], "answer": "O(m+n)"}
    ],
    "DBMS": [
        {"question": "What does SQL stand for?", "options": ["Structured Query Language", "Simple Query Language", "Standard Query Language"], "answer": "Structured Query Language"},
        {"question": "Which of these is not a type of database?", "options": ["Relational", "Distributed", "Tree"], "answer": "Tree"},
        {"question": "Which command is used to retrieve data?", "options": ["INSERT", "UPDATE", "SELECT"], "answer": "SELECT"},
        {"question": "Which key is used to uniquely identify rows?", "options": ["Foreign key", "Primary key", "Candidate key"], "answer": "Primary key"},
        {"question": "Which is a type of JOIN?", "options": ["FULL JOIN", "SEMI JOIN", "PARTIAL JOIN"], "answer": "FULL JOIN"},
        {"question": "What is the command to delete all rows from a table?", "options": ["TRUNCATE", "DELETE", "DROP"], "answer": "TRUNCATE"},
        {"question": "Which normal form eliminates multivalued dependencies?", "options": ["2NF", "3NF", "4NF"], "answer": "4NF"},
        {"question": "What does ACID stand for?", "options": ["Atomicity, Consistency, Isolation, Durability", "Accuracy, Consistency, Integrity, Durability"], "answer": "Atomicity, Consistency, Isolation, Durability"},
        {"question": "Which type of database scaling involves adding more servers?", "options": ["Vertical", "Horizontal", "Distributed"], "answer": "Horizontal"},
        {"question": "Which constraint enforces a unique value in a column?", "options": ["UNIQUE", "PRIMARY KEY", "FOREIGN KEY"], "answer": "UNIQUE"}
    ],
    "Python": [
        {"question": "What is the output of '3 * 'abc'?", "options": ["'abcabcabc'", "'abc*3'", "Error"], "answer": "'abcabcabc'"},
        {"question": "Which of these is a mutable type?", "options": ["Tuple", "List", "String"], "answer": "List"},
        {"question": "Which function is used to convert a string to lowercase?", "options": ["lower()", "downcase()", "toLower()"], "answer": "lower()"},
        {"question": "Which of these is a loop structure?", "options": ["if", "for", "print"], "answer": "for"},
        {"question": "Which method is used to add an element to a list?", "options": ["add()", "append()", "insert()"], "answer": "append()"},
        {"question": "What is the output of 'len([1, 2, 3])'?", "options": ["3", "2", "4"], "answer": "3"},
        {"question": "What does 'import math' do?", "options": ["Imports the math module", "Defines math operations", "Starts math interpreter"], "answer": "Imports the math module"},
        {"question": "Which keyword is used for a function?", "options": ["func", "function", "def"], "answer": "def"},
        {"question": "What is the output of 'print(2 ** 3)'?", "options": ["6", "8", "9"], "answer": "8"},
        {"question": "What is the default data type of a number in Python?", "options": ["int", "float", "double"], "answer": "int"}
    ]
}

# Ensure files exist with appropriate permissions
try:
    open(users_file, "a").close()
    open(results_file, "a").close()
except PermissionError:
    print(f"Permission denied: Unable to access {users_file} or {results_file}. Check permissions or directory.")
    exit(1)

# User registration
def register():
    print("Enter your details to register:")
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    full_name = input("Full Name: ").strip()
    age = input("Age: ").strip()
    email = input("Email: ").strip()
    phone = input("Phone Number: ").strip()
    
    with open(users_file, "a") as file:
        file.write(f"{username},{password},{full_name},{age},{email},{phone}\n")
    print("Registration successful!")

# User login
def login():
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    with open(users_file, "r") as file:
        for line in file:
            user_data = line.strip().split(',')
            if user_data[0] == username and user_data[1] == password:
                print("Login successful!")
                return username  # Return logged-in username
    print("Login failed. Please check your username and password.")
    return None

# Quiz attempt
def attempt_quiz(username):
    subject = input("Choose a subject: DSA, DBMS, Python: ").strip()
    if subject not in quizzes:
        print("Invalid subject choice.")
        return
    selected_questions = random.sample(quizzes[subject], 5)
    score = 0
    for q in selected_questions:
        print("\n" + q["question"])
        for i, option in enumerate(q["options"], start=1):
            print(f"{i}. {option}")
        try:
            answer = int(input("Enter the option number of your answer: ").strip())
            if 1 <= answer <= len(q["options"]) and q["options"][answer - 1] == q["answer"]:
                score += 1
        except (ValueError, IndexError):
            print("Invalid input. Moving to the next question.")
    print(f"\nYou scored {score} out of 5.")

    with open(results_file, "a") as file:
        file.write(f"{username},{subject},{score}/5\n")
    print("Your result has been saved.")

# Show all results
def show_results():
    print("\n--- Results ---")
    try:
        with open(results_file, "r") as file:
            for line in file:
                username, subject, score = line.strip().split(',')
                print(f"Name: {username}, Subject: {subject}, Score: {score}")
    except FileNotFoundError:
        print("No results found.")

# Main function
def main():
    logged_in_user = None
    while True:
        op = input("""\nChoose an option: 
        1. Register
        2. Login
        3. Attempt Quiz
        4. Show Results
        5. Exit
        Enter your choice: """).strip()
        
        if op == '1':
            register()
        elif op == '2':
            logged_in_user = login()
        elif op == '3':
            if logged_in_user:
                attempt_quiz(logged_in_user)
            else:
                print("Please log in to attempt a quiz.")
        elif op == '4':
            show_results()
        elif op == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function
main()
