# The job for today is to create a Pomodoro App
# I have started late today as well but I'm pretty sure I'll be able to finish
# by midnight. The starting constants were set from the course, and it has
# divided the coding part into sections so I'll just keep it like that maybe

from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
time_var = None
# We can't set timer to any value yet, so we just set it to None
# ---------------------------- TIMER RESET ------------------------------- # 
# Finally, we need a way to reset the timer and everything else to the start value
# For that, we will need to stop the after() that is currently running and changing
# the counter values. To do that we can use after_cancel() but we need a variable
# as its argument so we will create a timer variable and it will contain the after()
def reset_timer():
    window.after_cancel(time_var)
    # Now we need to reset all values to their default
    canvas.itemconfig(timer, text = "00:00")
    heading_text.config(text = "Timer", fg = GREEN)
    checkmark.config(text = "")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
# We need a way to initialize the timer on command, so that we can bind it to the click
# of the start button. So let me just do that
def counter_start():
    global reps
    
    # The Pomodoro we're implementing works this way:
    # 25 min work -> 5 min break 3 times, then 25 min work and then long 20 min break
    # Let's first get the number of seconds in order
    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60
    
    # Now we need to make it so that depending on the rep we're on, we will call the
    # appropriate count function for that amount of time
    # Another challenge is to update the label depending on whether it is work or break
    # while reps<9:
    reps += 1
    if reps%2 == 1:
        # This is for the work time, which are all uniform in odd'th rep places
        heading_text.config(text = "Work", fg = GREEN)
        time_counter(work_secs)
    elif reps == 8:
        heading_text.config(text = "Break", fg = RED)
        time_counter(long_break_secs)
        # I don't know whether this should be in the final code but adding just in case
        # I could instead do reps = (reps + 1) % 8 above during increment but meh
    else:
        heading_text.config(text = "Break", fg = PINK)
        time_counter(short_break_secs)
    # I failed to make it so the timer switches from one to the other, the loop misbehaved
    # Maybe I can use a recursion to do the loop though
    # if reps < 9:
    #     counter_start()
    # It still looks like all of the counters are trying to run at the same time. Why though
    # I don't know exactly why it didn't work here, but maybe the time_counter function
    # doesn't return cleanly into this function when it ends, so we'll just start the timer
    # at the end of that count down function
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# Now that this UI thing is donw, let's create a countdown mechanism for the timer
# Since GUI programs are event driven i.e. need to keep listening to events all the time
# We can't just use a sleep() function here, that would cause the program to misbehave
# Since we use it inside a loop, we won't be able to make it do any other thing while it
# is going on. That is why Tkinter contains a method called after()

# The after() has two main arguments
# The course had a sort of a basic structure, but I'll try to make the full blown version
def time_counter(count):
    global time_var
    # I have used the timer variable before being declared so I had to bring it before that
    mins = math.floor(count/60)
    # I had thought of using floor() but I didn't think the course had used it so I stuck
    # with integer conversion, but since it was introduced, it might be better to use it
    seconds = count % 60
    # Python is a strongly typed language, meaning we can't perform operations on a data
    # if it doesn't match the data type the operation is meant for, it holds on to a type
    # But it is also dynamically typed, meaning, we can change the data type held by an
    # item/variable and then it will only support operations meant for that data type
    # The key thing is that we must change the type ourselves, else it stays the same
    # So to make 9 appear as 09 and so on, we change these integers to strings
    # This is in contrast to other statically typed languages like C, Java, etc where
    # we can't change the data type at all once defined.
    if seconds < 10:
        seconds = f"0{seconds}"
    # This was a challenge given in the course, and I think it was an effortless idea :)
    # And it was ditto the solution offered there, so that makes me happy.
    
    # Now we need to change the element in the canvas, we can't just use the same config
    # method we use for the labels. We need to first save the canvas element in a variable
    # then we can configure each element by getting hold of that variable
    canvas.itemconfig(timer, text = f"{mins}:{seconds}")
    # So far it just displays seconds in single digits, but I'm pretty happy with how it
    # has turned out so far, maybe the course will cover a way to solve that too.
    # So it seems the solution is dynamic typing.
    # It's so late, I might have to stop it at this, and later update the post once it's
    # all done. So much for the whole initial confidence.
    
    if count>0:
        # I used two variables for mins and seconds, but the course has only one, maybe
        # that would be better than having to make multiple logic for these
        # If I didn't make it a global variable, I wouldn't be able to access it outside
        # of here, so that I could stop the timer when using reset button
        time_var = window.after(1000, time_counter, count - 1)
        # We can see the first one is the time in ms, second is the function, here we take
        # help of recursion to get the job done. Next is *args, where we can supply as many
        # arguments as we like and they'll be supplied to the function that is called
    else:
        counter_start()
        # This should get the next rep going and complete the loop finally
        # It is possible that when I was using loops with the last one, it was running the
        # loops more concurrently than it seemed. Maybe I'll ask ChatGPT later
        # But at least this method ensures the next rep doesn't begin until this one's over
        if reps%2 == 0:
            # At the end of every 2 reps, a cycle of work is completed
            # So we need to add a checkmark to the checkmark label
            # checks += "✔️"
            # I forgot we were doing this inside a function so it would be a local variable
            # we need to create the checks on the spot and the label text stays
            checks = ""
            for _ in range(math.floor(reps/2)):
                checks += "✔️"
            checkmark.config(text = checks)

# We can then later call the function to set mins and secs initially and go from there

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro-chan")
# window.minsize(width = 800, height = 600)
# After looking at the lesson, I thought I might want to have this set itself up
window.config(padx = 150, pady = 100, bg = YELLOW)
# The background color for the window can be set using the bg argument
# The color palette can be extracted from https://colorhunt.co/

# Now we need a Canvas widget in order to place a picture of a tomato inside the window
# The canvas allows us to put elements stacked on top of each other
canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness = 0)
# The canvas by default has a white border and a white background so we can change it
# by setting the background to yellow and the border thickness to 0
# The pixel width and height are to match the tomato image's resolution 200x223
tomato_image = PhotoImage(file = "day-28-pomodoro-app/tomato.png")
canvas.create_image(100, 112, image = tomato_image)
# The two values here are the position of the image in the canvas. By setting the values
# to the half of the canvas resolution, the center of the image will coincide with the
# center of the canvas and the image will fit perfectly inside the canvas
# If the image didn't fit, the image would appear cut off on any one side.
timer = canvas.create_text(100, 130, text = "00:00", fill = "white",
                   font = (FONT_NAME, 25, "bold"))
# The text will appear over the image and we can configure the text as we like
# The value for the positions are *args and the other properties are **kwargs
# Position is mostly trial and error, tkinter is not heavily documented

# I forgot everything needs to have a layout to actually appear on the screen
canvas.grid(column = 1, row = 1)
# The grid format is my attempt at replicating the grid shown in the course

# The challenge now is to complete the UI layout with the following components:
# 1. A label that says "Timer" in green, above the tomato
# 2. Two buttons, for start and reset on either side of the bottom of tomato
# 3. A checkmark label on the bottom that indicates number of cycles completed
# Note that we are only working with UI at first, the actions will be added later

heading_text = Label(text = "Timer", fg = GREEN, bg = YELLOW, font = (FONT_NAME, 50))
# Also since we have many elements and a desired layout format, it seems better
# to use grid instead of pack, so I'll change the canvas above to grid as well
heading_text.grid(column = 1, row = 0)


start_btn = Button(text = "Start", highlightthickness = 0, command = counter_start)
# One bug that is still lingering after it is all done is that if I press the start
# button twice, it will change from work to break
# I don't know how to fix it though
start_btn.grid(column = 0, row = 2)


reset_btn = Button(text = "Reset", highlightthickness = 0, command = reset_timer)
reset_btn.grid(column = 2, row = 2)
# Looks like the buttons look different in Windows and Mac so it looks kinda different
# as compared to the one in the course, I'll just have to make do with this for now.

checkmark = Label( fg = GREEN, bg = YELLOW, font = (FONT_NAME, 20))
# Initially there will be no checkmark
# checkmark.config(justify = "center")
# This was something I added randomly
checkmark.grid(column = 1, row = 3)

window.mainloop()