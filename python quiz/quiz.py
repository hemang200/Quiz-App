# In-memory storage for users and results
users = {}
results = {}

# Quiz questions
quizzes = {
    "DSA": [
        {"question": "What is the time complexity of binary search?", "options": ["O(n)", "O(log n)", "O(n^2)"], "answer": "O(log n)"},
        {"question": "Which data structure is used in BFS?", "options": ["Stack", "Queue", "Tree"], "answer": "Queue"},
        {"question": "What is the worst-case time complexity of quicksort?", "options": ["O(n^2)", "O(n log n)", "O(n)"], "answer": "O(n^2)"},
        {"question": "Which of the following is not a linear data structure?", "options": ["Array", "Tree", "Linked List"], "answer": "Tree"},
        {"question": "Which data structure allows LIFO?", "options": ["Queue", "Stack", "Array"], "answer": "Stack"}
    ],
    "DBMS": [
        {"question": "What does SQL stand for?", "options": ["Structured Query Language", "Simple Query Language", "Standard Query Language"], "answer": "Structured Query Language"},
        {"question": "Which of these is not a type of database?", "options": ["Relational", "Distributed", "Tree"], "answer": "Tree"},
        {"question": "Which command is used to retrieve data?", "options": ["INSERT", "UPDATE", "SELECT"], "answer": "SELECT"},
        {"question": "Which key is used to uniquely identify rows?", "options": ["Foreign key", "Primary key", "Candidate key"], "answer": "Primary key"},
        {"question": "Which is a type of JOIN?", "options": ["FULL JOIN", "SEMI JOIN", "PARTIAL JOIN"], "answer": "FULL JOIN"}
    ],
    "Python": [
        {"question": "What is the output of '3 * 'abc'?", "options": ["'abcabcabc'", "'abc*3'", "Error"], "answer": "'abcabcabc'"},
        {"question": "Which of these is a mutable type?", "options": ["Tuple", "List", "String"], "answer": "List"},
        {"question": "Which function is used to convert a string to lowercase?", "options": ["lower()", "downcase()", "toLower()"], "answer": "lower()"},
        {"question": "Which of these is a loop structure?", "options": ["if", "for", "print"], "answer": "for"},
        {"question": "Which method is used to add an element to a list?", "options": ["add()", "append()", "insert()"], "answer": "append()"}
    ]
}

# User registration
def register():
    print("Enter your details to register:")
    username = input("Username: ").strip()
    if username in users:
        print("Username already exists. Please choose a different username.")
        return
    password = input("Password: ").strip()
    full_name = input("Full Name: ").strip()
    age = input("Age: ").strip()
    email = input("Email: ").strip()
    phone = input("Phone Number: ").strip()
    users[username] = {"password": password, "full_name": full_name, "age": age, "email": email, "phone": phone}
    print("Registration successful!")

# User login
def login():
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    if username in users and users[username]["password"] == password:
        print("Login successful!")
        return username
    print("Login failed. Please check your username and password.")
    return None

# Quiz attempt
def attempt_quiz(username):
    subject = input("Choose a subject: DSA, DBMS, Python: ").strip()
    if subject not in quizzes:
        print("Invalid subject choice.")
        return
    score = 0
    for q in quizzes[subject]:
        print("\n" + q["question"])
        for i, option in enumerate(q["options"], start=1):
            print(f"{i}. {option}")
        try:
            answer = int(input("Enter the option number of your answer: ").strip())
            if 1 <= answer <= len(q["options"]) and q["options"][answer - 1] == q["answer"]:
                score += 1
        except (ValueError, IndexError):
            print("Invalid input. Moving to the next question.")
    print(f"\nYou scored {score} out of {len(quizzes[subject])}.")
    if username not in results:
        results[username] = []
    results[username].append({"subject": subject, "score": score, "total": len(quizzes[subject])})
    print("Your result has been saved.")

# Show all results
def show_results():
    print("\n--- Results ---")
    if not results:
        print("No results found.")
        return
    for username, user_results in results.items():
        for result in user_results:
            print(f"Name: {username}, Subject: {result['subject']}, Score: {result['score']}/{result['total']}")

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
