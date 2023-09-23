import turtle
import pandas
from state_name import StateName
from scoreboard import Scoreboard
import time

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.tracer(0)

screen.addshape(image)
turtle.shape(image)
scoreboard = Scoreboard()

data = pandas.read_csv("50_states.csv")
states_list = data["state"].tolist()
guessed_states = []

while len(states_list) <= 50:
    time.sleep(0.1)
    screen.update()
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
    answer_state = answer_state.title()

    if answer_state == "Exit":
        missing_states = [state for state in states_list if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in states_list:
        StateName(answer_state)
        guessed_states.append(answer_state)
        scoreboard.right_answer()
