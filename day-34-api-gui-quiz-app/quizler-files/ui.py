# We have used Tkinter to create GUI Applications but we have done it without
# making use of classes apart from the ones offered by Tkinter. In this quiz app,
# everything is divided into classes and called in the main.py so we need to have a
# class for the GUI as well.

from tkinter import *
# Since our QuizBrain class is reponsible for all the question handling, let's import it here
from quiz_brain import QuizBrain
# This is imported so that since we need to pass the question information to the UI, we can let
# the program know that QuizBrain is the datatype associated with the argument we're passing

THEME_COLOR = "#375362"

class QuizApp:
    
    def __init__(self, quiz_brain: QuizBrain):
        # This second parameter allows us to set a required data type for the quiz_brain arg
        # And it will show an error if we pass something else as an argument in the calling line in main
        self.quiz = quiz_brain
        
        self.window = Tk()
        self.window.title("GUI Quiz-chan")
        self.window.config(padx = 20, pady = 20, bg = THEME_COLOR)
        
        # The course hasn't brought this up yet, but let's get this over with        
        # I don't know if this is the best way to do it but here goes.
        self.wait = self.window.after(0, self.show_next_question)
        
        # Now let's have the UI setup in some method here:
        self.setup_ui()
        # We now need to show the next question
        self.show_next_question()
        
        self.window.mainloop()
        
    def setup_ui(self):
        """Here the UI is setup as close to the course slides as possible from me"""
        # First the score label on top:
        self.score_label = Label(text = f"Score: 0", bg = THEME_COLOR, fg = "white", font = ("Arial"))
        # At first I'll leave the score as 0, then later add a variable probably
        self.score_label.grid(row = 0, column = 1)
        
        # Now turn for the canvas in the middle
        self.canvas = Canvas(width = 300, height = 250, bg = "white")
        self.question_text = self.canvas.create_text(
                                                    150, 125, 
                                                     text = f"",
                                                     font = ("Arial", 20, "italic"),
                                                     width = 280,
                                                     fill = THEME_COLOR)
        # The width property will ensure our text will wrap once it exceeds the given width, which we have
        # set to be a bit smaller than the canvas width
        self.canvas.grid(row = 1, column = 0, columnspan = 2, pady = 50)
        # I didn't have the pady, but I guessed it would be necessary though, so added after the
        # course showed how to
        
        # Finally the buttons
        self.true_img = PhotoImage(file = "day-34-api-gui-quiz-app/quizler-files/images/true.png")
        self.false_img = PhotoImage(file = "day-34-api-gui-quiz-app/quizler-files/images/false.png")
        self.true_btn = Button(image = self.true_img, highlightthickness = 0, borderwidth = 0,
                               bg = THEME_COLOR, command = self.user_input_true)
        self.false_btn = Button(image = self.false_img, highlightthickness = 0, borderwidth = 0,
                                bg = THEME_COLOR, command = self.user_input_false)
        self.true_btn.grid(row = 2, column = 0)
        self.false_btn.grid(row = 2, column = 1)
        # For some reason my buttons just refuse to appear on the screen. Let's see if the course
        # provides any hint, I tried to recreate the code in my last project but it didn't go as expected
        # Ok my fault was creating a function to do this since if I had done it in init, I wouldn't have
        # had to set the scope of the images to the whole class, but since I'm doing it inside a function
        # and the images are supposed to be a part of Tk which is defined in __init__, I had to give them
        # a higher scope. Alright my bad then, I didn't realize it before but I realized it myself so yay
    
    def show_next_question(self):
        self.window.after_cancel(self.wait)
        # The course didn't have this line, I added it in vain, but why was it not necessary?
        self.canvas.config(bg = "white")
        self.canvas.itemconfig(self.question_text, fill = THEME_COLOR)
        self.score_label.config(text = f"Score: {self.quiz.score}")
        
        # When we reach the end of the quiz, we need to let the user know it is the end
        # Fortunately, we already have a method in our quiz_brain file for that
        if self.quiz.still_has_questions():
            self.question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text = self.question)
        else:
            self.canvas.itemconfig(self.question_text, 
                text = f"You have reached the end of the quiz\nYour final score was: {self.quiz.score}\nThanks for playing!")
            self.true_btn.config(state = "disabled")
            self.false_btn.config(state = "disabled")
            # By disabling these buttons, we prevent the user from being able to still call the functions
            # when they press the buttons on the quiz completed page
        
    # To add functionality to the buttons we need to call the check_answer() method in the quiz_brain file
    # but the course suggested I make two different methods to do this, so I'll just have to comply
    # Else I would've tried to pass the arguments right from the Button class, I'm not completely sure
    # whether the method I think works or not but I'll try it later, I don't have too much time in my hands
    def user_input_true(self):
        if self.quiz.check_answer("True"):
            self.show_feedback(True)
        else:
            self.show_feedback(False)
        
    
    def user_input_false(self):
        # I could do it like the method above, or I had forgotten this was possible too:
        self.show_feedback(self.quiz.check_answer("False"))
        # Also my method seems almost the same as the one in the course, now we'll have to see
        # how the canvas background is handled.
        
        
    def show_feedback(self, correct: bool):
        if correct:
            self.canvas.config(bg = "green")
        else:
            self.canvas.config(bg = "red")
        self.canvas.itemconfig(self.question_text, fill = "white")
        
        self.wait = self.window.after(300, self.show_next_question)
        
    # Looks like I completed the app(almost) without having to look at the course after I was
    # instructed to set up the button behaviour, but I think I might give combining the two methods
    # into a single one a go
    # I looked up in google, but it showed me I had to use a lambda, since I think that is as of yet
    # out of the scope of my learning, I will not try to learn it yet, maybe later
    # But I will create a new function that will get rid of the repititive code for me
    # I thought of an idea, why not I add it all to the update score method, that way I don't have to
    # create a new function for every small thing