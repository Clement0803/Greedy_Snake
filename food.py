import random
from turtle import Turtle


class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.speed("fastest")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.refresh()
        self.active = True
    
    def refresh(self):
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)
        
    def bonus_food(self):
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)
        self.color("gold")
    
    def hide(self):
        self.is_active = False
        self.hideturtle()

    def show(self):
        self.is_active = True
        self.showturtle()
        
    