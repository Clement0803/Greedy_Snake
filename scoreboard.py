from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        with open("Simple_Project/snake_game/data.txt") as data:
            self.high_score = int(data.read())
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score:{self.high_score}", align="center", font=("Courier", 18, "normal"))
        
    def reset(self):
            if self.score > self.high_score:
                self.high_score = self.score
                with open("Simple_Project/snake_game/data.txt", mode="w") as data:
                    data.write(f"{self.high_score}")
            
            self.score = 0
            self.update_scoreboard()
            
    def increase_score(self,points=1):
        self.score += points
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 36, "normal"))
    
   
        
        

    
    

