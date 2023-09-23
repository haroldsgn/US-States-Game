from turtle import Turtle
import pandas


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.data = pandas.read_csv("50_states.csv")
        self.states_list = self.data["state"].tolist()
        self.states_amount = len(self.states_list)
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 245)
        self.write(f"{self.score}/{self.states_amount}", align="center", font=("Courier", 25, "bold"))

    def right_answer(self):
        self.score += 1
        self.update_scoreboard()


