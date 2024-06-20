from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# We need to create a question_bank list which contains objects of the
# class Question, that will be imported from the question_data list
question_bank = []
for question in question_data:
    question_bank.append(Question(question["question"], question["correct_answer"]))
# Okay this should be good enough.

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
    
# Now after the game is finished we need to print out the score
print("Nice! You've completed the quiz.")
print(f"Your final score is: [{quiz.score}/{quiz.q_no}]")

# Next is utilizing an API to get questions from another source
# All that will be in the data file