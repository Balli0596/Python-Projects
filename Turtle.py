import turtle
import random
import time

WIDTH,HEIGHT=500,750
colors=["red","blue","green","yellow","orange","purple","pink","brown","cyan","magenta"]   
 
def setup_screen():

    
    
    
    screen=turtle.Screen()
    screen.title("racing game")
    screen.bgcolor("black")
    screen.setup(width=WIDTH,height=HEIGHT)
def create_turtle(colors__ofturtle):
    turtles=[]
    spacing=WIDTH//len(colors__ofturtle)+1
    for i,color in enumerate(colors__ofturtle):
        racer=turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")    
        racer.left(90)
        
        racer.penup()
        racer.setpos(-(WIDTH//2)+spacing*i+1,-HEIGHT//2+50)
        racer.pendown()
        turtles.append(racer)
    return turtles
def race(colors__ofturtle):
    turtles=create_turtle(colors__ofturtle)
    while True:
        for racer in turtles:
            distance=random.randint(1,10)
            racer.forward(distance)
            if racer.ycor()>=HEIGHT//2-50:
                print(f"{racer.color()[0]} turtle wins!")
                return
        






def get_no_of_racers():
    while True:
        racers=input("Enter the number of racers (2-10): ")
        if(racers.isdigit() and 2<=int(racers)<=10):
            return int(racers)
        else:
            print("invalid input.please enter valid statemnet")
            continue
racers=get_no_of_racers()
setup_screen()
random.shuffle(colors)
colors__ofturtle=colors[:racers]
winner=race(colors__ofturtle)





turtle.done()