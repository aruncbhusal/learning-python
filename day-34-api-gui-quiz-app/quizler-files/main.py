# Today we'll be working with the same CLI based quiz app we created on Day 17
# and turning it into a GUI Yes/No trivia game, this time using API
# The starting code is basically the same as on day 17, so this is from the course
# Any changes made will be marked in the individual files with their appropriate comments
# I will also list the changes here:

# 1. In data.py, the question_data dictionary now extracts data directly from OpenTrivia API
#    which used to be hardcoded and fixed for every run of the program


from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizApp

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
# Let's call the GUI here, after the brains is ready
app = QuizApp(quiz)
# Since this has a mainloop() which is basically an infinite while loop that checks
# for any updates to refresh the screen, we shouldn't have a while loop near it, it may misbehave

# while quiz.still_has_questions():
#     quiz.next_question()

# print("You've completed the quiz")
# print(f"Your final score was: {quiz.score}/{quiz.question_number}")
