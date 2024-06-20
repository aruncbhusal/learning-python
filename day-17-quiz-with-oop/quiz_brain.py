# In this file, we have a QuizBrain class which does the
# full functionality of question serving, checking, etc
class QuizBrain:
    def __init__(self, question_list):
        # The question number should default start at 0
        self.q_no = 0
        self.q_list = question_list
        # We need a new attribute for the current score
        self.score = 0
        
    # Next out job is to create the next_question() module
    # It will be used to ask the question from question number
    def next_question(self):
        question = self.q_list[self.q_no]
        # Originally, I had used increment on q_no in the input line
        # But the question number needs to get incremented anyway
        # So just like the course, I did this too:
        self.q_no += 1
        reply = input(f"Q.{self.q_no}: {question.text} (True/False): ").lower()
        # Since this function is responsible for serving questions
        # We will also call the check answer here
        self.check_answer(reply, question.answer)
        
    # Now our job is to serve questions until the end of question bank
    def still_has_questions(self):
        return (self.q_no < len(self.q_list))
        # Only when we reach the last element is there no next question
        # Rather than using if .. then True else False, we can simplify
        
    # We also need a method to check the answer
    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            print("Yay! You got it right!")
            self.score += 1
        else:
            print("That was incorrect!")
        print(f"The correct answer was {correct_answer}")
        print(f"Your score stands at [{self.score}/{self.q_no}]\n")