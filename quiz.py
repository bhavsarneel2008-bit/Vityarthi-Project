def python_quiz():
    print("\n===== PYTHON QUIZ =====")
    questions = [
        ("Which keyword is used to define a function?", "def"),
        ("Which function is used to take input?", "input"),
        ("Which symbol is used for comments?", "#"),
        ("Which function is used to display output?", "print"),
        ("Which keyword is used to stop a loop?", "break")
    ]
    score = 0
    for question, answer in questions:
        print("\n" + question)
        user_answer = input("Your answer: ").lower()
        if user_answer == answer:
            print("Correct!")
            score = score + 1
        else:
            print("Wrong!")
            print("Correct answer:", answer)
    print("\nYour final score is:", score, "/", len(questions))
    return "Python Quiz - " + str(score) + "/" + str(len(questions))

