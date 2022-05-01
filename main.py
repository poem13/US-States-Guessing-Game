import turtle
import pandas

screen = turtle.Screen()
screen.title("US STATES GAME")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

score = 0
data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
guessed_states = []

while True:
    answer = screen.textinput(title=f"Guess the State: {score}/50", prompt="What's another state's name?")
    if answer.lower() == "exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer in all_states:
        x = int(data[data["state"] == answer].x)
        y = int(data[data["state"] == answer].y)
        #Create a turtle
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data["state"] == answer]
        t.goto(x, y)
        t.write(answer)
        score += 1

#states missing to csv
turtle.mainloop()