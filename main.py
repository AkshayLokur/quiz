from data import question_data
from Question import Question
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    question_bank.append(Question(item["question"], item["correct_answer"]))

qb = QuizBrain(question_bank)
while qb.still_has_questions():
    qb.next_question()
else:
    print("\n⇣⇣⇣⇣⇣⇣⇣⇣⇣⇣⇣⇣⇣⇣⇣⇣⇣⇣⇣⇣⇣⇣⇣⇣⇣⇣⇣⇣⇣⇣⇣⇣⇣⇣⇣⇣⇣⇣⇣⇣⇣⇣⇣⇣⇣⇣⇣⇣⇣⇣⇣⇣⇣⇣⇣⇣⇣⇣")
    print("You've completed the Quiz!")
    print(f"Your final score is: {qb.score} / {len(qb.question_list)}")
