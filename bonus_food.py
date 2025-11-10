from turtle import Screen, Turtle
import random

class BonusFood(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("gold")
        self.speed("fastest")
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.refresh()
        self.active = False
    
    def refresh(self):
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)
        
    def activate(self):
        self.active = True
        self.refresh()
        self.showturtle()
        
    def deactivate(self):
        self.active = False
        self.hideturtle()