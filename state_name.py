from turtle import Turtle
import pandas


class StateName:
    def __init__(self, answer_state):
        self.data = pandas.read_csv("50_states.csv")
        self.state_row = self.data[self.data.state == answer_state]
        self.state = self.state_row.state.prod()
        self.x_position = self.state_row.x.prod()
        self.y_position = self.state_row.y.prod()
        self.state_name = Turtle()
        self.state_name.color("Black")
        self.state_name.penup()
        self.state_name.hideturtle()
        self.state_name.goto(self.x_position, self.y_position)
        self.state_name.write(self.state, align="center", font=("Courier", 7, "normal"))

