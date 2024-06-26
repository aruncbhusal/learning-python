# In the final challenge for today, we will be creating a game where
# we have to guess the states of USA. And the states guessed will appear
# on an initially empty map of the US. Turtle will be used to create the game
# but we will use pandas to get the game working.
# turtle only supports .gif files so the map is .gif. I have downloaded the
# starting files from the course resources and will be building on top of it

import turtle as t
import pandas

screen = t.Screen()
screen.title("Guess the States!")
image = "day-25-csv-with-pandas/us-states-game/blank_states_img.gif"
screen.addshape(image)
t.shape(image)

# In order to get the co ordinates of a mouse click on screen, we can use
# screen.onscreenclick(function)
# This function will have two arguments x and y and if we return them
# They will contain the on screen co ordinates of the click.
# But that is already taken care of in the 50_states.csv file

input_state = screen.textinput(title= "Name a state",
                               prompt= "What state do you have in mind now?").title()

# Let's import the csv first
states_file = pandas.read_csv("day-25-csv-with-pandas/us-states-game/50_states.csv")

def reveal_state(name):
    state_name = t.Turtle()
    state_name.shape("turtle")
    state_name.color("black")
    state_name.up()
    state_name.hideturtle()
    state_row = states_file[states_file.state == name]
    co_ords = (state_row.iloc[0].x,state_row.iloc[0].y)
    # The course instead had the following LOC but it says the option to turn
    # a single serial data into int is being deprecated so what I did is better
    # at least at this point in time:
    # co_ords = (int(state_row.x),int(state_row.y))
    
    # I didn't really understand the documentation well for iloc so I took help
    # from ChatGPT so I guess I cheated but well, I didn't have to watch the video
    # for it so it's a win I guess?
    # Actually, now that I look at the error, I can see what it meant. Silly me
    state_name.goto(co_ords)
    state_name.write(arg= name, align="center", font= ("Arial", 8, "normal"))
    # I could just use state_name.write(name) since all others are default anyway
    # state_name.write(state_row.state.item()) is valid as well, the item() method
    # in the pandas Series type returns the actual first item in the series
    return state_name

game_finished = False
states_list = states_file.state.to_list()
guessed_states = []
guess_list = []
while not game_finished:
    # for name in states_file.state:
    # # In the course, instead of this, a list was created that held all the state names
    # # extracted from the csv using .to_list()
    #     # print(input_state)
    #     # print(name)
    #     if input_state == name:
    #         correct += 1
    #         guessed_states.append(reveal_state(name))
    
    if input_state == "Exit":
        # screen.textinput("One More Thing", "The states you missed are stored in a CSV!")
        break
        # I can't believe it took this long to get introduced to this statement
        # I had been holding myself from using it until after I've actually seen it being
        # used inside the course, now I am free from my shackles, finally.
    
    if input_state in states_list:
        guess_list.append(input_state)
        guessed_states.append(reveal_state(input_state))
            
    if len(guessed_states) == 50:
        game_finished = True
        screen.textinput("Bye Bye", "Thanks for playing!")
    else:
        input_state = screen.textinput(title= f"[{len(guessed_states)}/50] Guessed. Keep Going!",
                                   prompt= "How about one more?").title()

# Final challenge was to create a csv that contains all the states the user missed
remaining_states = []
for state in states_list:
    if not state in guess_list:
        remaining_states.append(state)
rem_state = pandas.DataFrame(remaining_states)
rem_state.to_csv("day-25-csv-with-pandas/us-states-game/remaining_states.csv")

# t.mainloop()
# had to remove this since we want to exit when we break free of the loop
# This acts as a replacement to exitonclick() since we might click on the map
# but we don't want the screen to close because of it