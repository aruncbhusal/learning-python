from html import unescape

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    # When displaying our question as is, some characters look weird, that is because they are HTML
    # Entities, used to replace some characters since during HTML decoding, they might be confused
    # for the characrers used to build the HTML.
    # In order to get them to their actual character, we must "unescape" those entities.
    # In python, the html module provides an unescape() method to do just that
    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        
        current_q = unescape(self.current_question.text)
        
        return f"Q.{self.question_number}: {current_q} (True/False): "
        # Since we're passing the next question to the UI, we don't need the input section anymore
        # user_answer = input(f"Q.{self.question_number}: {self.current_q} (True/False): ")
        # self.check_answer(user_answer)

    def check_answer(self, user_answer) -> bool:
        # I just learned about type hints so I will definitely use it where I can
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
            # print("You got it right!")
        else:
            return False
            # print("That's wrong.")

        # print(f"Your current score is: {self.score}/{self.question_number}")
        # print("\n")
