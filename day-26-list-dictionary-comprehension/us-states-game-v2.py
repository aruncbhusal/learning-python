import turtle as t
import pandas

screen = t.Screen()
screen.title("Guess the States!")
image = "day-25-csv-with-pandas/us-states-game/blank_states_img.gif"
screen.addshape(image)
t.shape(image)

input_state = screen.textinput(title= "Name a state",
                               prompt= "What state do you have in mind now?").title()

states_file = pandas.read_csv("day-25-csv-with-pandas/us-states-game/50_states.csv")

def reveal_state(name):
    state_name = t.Turtle()
    state_name.shape("turtle")
    state_name.color("black")
    state_name.up()
    state_name.hideturtle()
    state_row = states_file[states_file.state == name]
    co_ords = (state_row.iloc[0].x,state_row.iloc[0].y)
    state_name.goto(co_ords)
    state_name.write(arg= name, align="center", font= ("Arial", 8, "normal"))
    return state_name

game_finished = False
states_list = states_file.state.to_list()
guessed_states = []
guess_list = []
while not game_finished:
    
    if input_state == "Exit":
        break
    
    if input_state in states_list:
        guess_list.append(input_state)
        guessed_states.append(reveal_state(input_state))
            
    if len(guessed_states) == 50:
        game_finished = True
        screen.textinput("Bye Bye", "Thanks for playing!")
    else:
        input_state = screen.textinput(title= f"[{len(guessed_states)}/50] Guessed. Keep Going!",
                                   prompt= "How about one more?").title()

# The line below is the only thing changed in this version. I incorporated the list comprehension
# method by removing the standalone for loop
remaining_states = [state for state in states_list if not state in guess_list]

rem_state = pandas.DataFrame(remaining_states)
rem_state.to_csv("day-25-csv-with-pandas/us-states-game/remaining_states.csv")