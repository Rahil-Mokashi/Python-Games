from turtle import Turtle, Screen 
import pandas 
from PIL import Image

img = Image.open("iamge.gif")
resized = img.resize((1200, 800))
resized.save("world_map.gif")

screen  = Screen()
screen.setworldcoordinates(-180, -90, 180, 90)
screen.setup(width=1200, height=800)

entire_database = pandas.read_csv('countries.csv')

entire_database['x'] = entire_database['longitude'] * (1200 / 360)
entire_database['y'] = entire_database['latitude']  * (800 / 180)

final = entire_database[['COUNTRY', 'x', 'y']]
final.to_csv('country_turtle_coords.csv', index=False)



screen.bgpic("world_map.gif")



full_data = pandas.read_csv("country_turtle_coords.csv")

countries = full_data.COUNTRY.to_list()

guessed_countires = []

while len(countries) < 250:
    
    guess_country = screen.textinput(title=f"{len(guessed_countires)}/249 Countries Correct", prompt="What's another country name?").title()
    
    if guess_country == "Exit":
        missing_countries = []
        for country in countries:
            if country not in guessed_countires:
                missing_countries.append(country)
            
        missed_countries = pandas.DataFrame(missing_countries)
        missed_countries.to_csv("missed_countries.csv")
             
        break
    
    if guess_country in countries:
        guessed_countires.append(guess_country)
        
        turtle = Turtle()
        turtle.hideturtle()
        turtle.penup()
        
        country_row = full_data[full_data['COUNTRY']==guess_country]
        
        x = country_row.x.item()
        y = country_row.y.item()
        
        turtle.goto(x, y)
        turtle.write(guess_country,  align="center", font=('Arial', 5, 'normal'))
    


