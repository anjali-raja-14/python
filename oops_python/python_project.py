from project_database import question_bank
from project_database import options

correct_answer = 0
print("*****************************************")
print("Hey, welcome to the quiz")

for question_num in range(len(question_bank)):
    print("*****************************************")
    print(question_bank[question_num]["question"])
    for i in options[question_num]:
        print(i)
    guess_num = input("Enter your answer (A/B/C): ").upper()
    if guess_num == question_bank[question_num]["answer"]:
        print("Correct answer!")
        correct_answer += 1
        print(f"{correct_answer}/3")
    else:
        print("Incorrect answer.")
        print(f"The correct answer is: {question_bank[question_num]['answer']}")
