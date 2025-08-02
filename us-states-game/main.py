from turtle import Turtle, Screen
import pandas

turtle = Turtle()
writer = Turtle()
writer.hideturtle()
writer.penup()
screen = Screen()
screen.title("U.S. States Gmes")
screen.setup(width=720, height=510)

image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)

full_data = pandas.read_csv("50_states.csv")  

states = full_data.state.tolist()

guessed_states = []

while len(guessed_states)< 50:
    answer_input = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state name?").title()
    
    if answer_input == "Exit":
        missing_states = []
        
        for state in states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        
        break
    
    if answer_input in states:
        guessed_states.append(answer_input)
        
        state_row = full_data[full_data['state'] == answer_input]
        
        writer.goto(state_row.x.item(), state_row.y.item())
        
        writer.write(answer_input, align="center", font=('Arial', 7, 'normal'))
        



