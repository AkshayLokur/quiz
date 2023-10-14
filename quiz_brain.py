from Question import Question


class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        if self.question_list is not None and self.still_has_questions():
            user_answer = input(f"\nQ.{self.question_number + 1}: {self.question_list[self.question_number].text}: "
                                f"[True/False]: ")
            self.question_number += 1
            self.check_answer(user_answer)

    def still_has_questions(self):
        return len(self.question_list) > self.question_number

    def check_answer(self, user_answer):
        if user_answer.lower() == self.question_list[self.question_number - 1].answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("Nope, that's wrong!")

        print(f"The correct answer was {self.question_list[self.question_number - 1].answer}")
        print(f"Your score is {self.score} / {self.question_number}")
