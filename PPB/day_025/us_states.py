# https://www.sporcle.com/games/g/states

import turtle
import pandas as pd

# def get_mouse_click_cor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_cor)
# turtle.mainloop()

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(width=800, height=600)
turtle.shape(image)

df = pd.read_csv("50_states.csv")
all_states = df.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = []

        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        # missing_states = [state for state in all_states if state not in guessed_states]

        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        state_data = df[df.state == answer_state]

        t.goto(state_data.x.item(), state_data.y.item())
        t.write(state_data.state.item())

screen.exitonclick()
