from turtle import Turtle, Screen
import pandas

turtle = Turtle()
writer = Turtle()
writer.hideturtle()
writer.penup()
screen = Screen()
screen.title("U.S. States Gmes")

image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)

full_data = pandas.read_csv("50_states.csv")  


num = 0

# screen.bgpic("blank_states_img.gif")
# screen.setup(width=730, height=500)


while num < 50:
    x = 0
    y = 0
    answer_input = screen.textinput(title=f"{num}/50 States Correct", prompt="What's another state name?").title()
    if answer_input in full_data['state'].values:
        num = num + 1
        
        state_row = full_data[full_data['state'] == answer_input.title()]
        
        x = int(state_row.iloc[0]['x'])
        y = int(state_row.iloc[0]['y'])
        
        
        writer.goto(x, y)
        writer.write(answer_input, align="center", font=('Arial', 7, 'normal'))






screen.exitonclick()