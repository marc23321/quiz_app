import random

score = 0
attempts = 0 


questions = [
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": {"A": "Earth", "B": "Mars", "C": "Jupiter", "D": "Venus"},
        "answer": "B"
    },
    {
        "question": "What does the len() function do in Python?",
        "choices": {"A": "Adds two numbers", "B": "Returns the number of characters or items", "C": "Prints output", "D": "Converts text to lowercase"},
        "answer": "B"
    },
    {
        "question": "Which data type is immutable in Python?",
        "choices": {"A": "List", "B": "Dictionary", "C": "Tuple", "D": "Set"},
        "answer": "C"
    },
    {
        "question": "What symbol is used to start a comment in Python?",
        "choices": {"A": "//", "B": "<!--", "C": "#", "D": "/*"},
        "answer": "C"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "choices": {"A": "func", "B": "define", "C": "function", "D": "def"},
        "answer": "D"
    }
]
print("============= Welcome =============")

def get_consent():
    while True:
        consent = input("\nPlease Enter to play or q to quit\n").strip().lower()

        if consent == "":
            return "play"
        elif consent == "q":
            return "quit"
        else:
            print("Invalid option. Press Enter to play or 'q' to quit.")
        


def display_answers(question_num):
    for key, value in questions[question_num]['choices'].items():
        print(f"{key}: {value}")

def display_questions(question_num):
   print(questions[question_num]['question'])

while True:
    action = get_consent()
    if action == 'quit':
        break

    question_num = random.randint(0, len(questions) - 1)
    print("===========================================")
    display_questions(question_num)
    display_answers(question_num)


    valid = {"A", "B", "C", "D"}
    ans = input("\nAnswer (A/B/C/D): ").strip().upper()

    while ans not in valid:
        print("Please enter A, B, C, or D.")
        ans = input("Answer (A/B/C/D): ").strip().upper()
    attempts += 1

   
    if ans == questions[question_num]['answer']:
        print("\nCorrect!")
        score += 1
    else:
        print("\nWrong Choice")
        print(f"The correct answer is {questions[question_num]['answer']}: {questions[question_num]['choices'][questions[question_num]['answer']]}")
    print(f"Score: {score}")   
     
print("============= Final Results =============")
if attempts:
    print(f"Attempts: {attempts}\nFinal score: {score}({score/attempts*100:.1f}%)")
else:
    print("No questions attempted. Goodbye!")



