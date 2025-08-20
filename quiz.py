# **Simple Python Quiz Game**

def quiz_game():
    print("Welcome to the Quiz Game!")
    print("Answer the following questions by typing the correct option (a, b, c, or d).")
    print()

    # Questions and answers
    questions = [
        {
            "question": "What is the capital of India?",
            "options": ["a) Mumbai", "b) New Delhi", "c) Kolkata", "d) Chennai"],
            "answer": "b"
        },
        {
            "question": "Which programming language is known as the 'language of AI'?",
            "options": ["a) Python", "b) Java", "c) C++", "d) Ruby"],
            "answer": "a"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["a) Earth", "b) Mars", "c) Jupiter", "d) Saturn"],
            "answer": "c"
        }
    ]

    score = 0

    # Loop through questions
    for i, q in enumerate(questions, start=1):
        print(f"Q{i}: {q['question']}")
        for option in q["options"]:
            print(option)
        user_answer = input("Your answer: ").lower()

        if user_answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.\n")

    # Final score
    print(f"Quiz Over! Your final score is {score}/{len(questions)}.")
    if score == len(questions):
        print("Excellent! You got all the answers right!")
    elif score > 0:
        print("Good job! Keep practicing to improve.")
    else:
        print("Better luck next time!")

# Run the quiz
quiz_game()