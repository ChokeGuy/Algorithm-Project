import turtle
from turtle import Turtle

class Pen(Turtle):
    def __init__(self):
        Turtle.__init__(self)   
        self.hideturtle()     
        self.shape("./images/wall.gif")     
        self.penup()
        self.speed(0)

class Player(Turtle):
    def __init__(self,walls):
        Turtle.__init__(self)
        self.shape("./images/player.gif")     
        self.penup()
        self.speed(0)
        self.walls = walls

class Treasure(Turtle):
    def __init__(self, x, y):
        Turtle.__init__(self)
        self.shape("./images/treasure.gif")     
        self.penup()
        self.speed(0)
        self.goto(x, y)  

    def destroy(self):
        self.hideturtle()

class Walk(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.hideturtle()
        self.shape("./images/walk.gif")     
        self.penup()
        self.speed(0)    

class White(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.hideturtle()
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
        

class Button():
    def __init__(self,x_cor,y_cor,length, width, message,index):#,get_map
        self.button = Turtle()
        self.button.hideturtle()
        self.button.pencolor('#111111')
        self.button.fillcolor('#F5F5DC')
        self.arrays = []
        self.button_x = x_cor 
        self.button_y = y_cor 
        self.buttonLength = length
        self.buttonWidth = width
        self.mode = 'light'
        self.message = message
        self.index = index

    def draw_button(self):
        self.button.penup()
        self.button.begin_fill()
        self.button.goto(self.button_x, self.button_y)
        self.button.goto(self.button_x + self.buttonLength, self.button_y)
        self.button.goto(self.button_x + self.buttonLength, self.button_y + self.buttonWidth)
        self.button.goto(self.button_x, self.button_y + self.buttonWidth)
        self.button.goto(self.button_x, self.button_y)
        self.button.end_fill()
        self.button.goto(self.button_x + 5, self.button_y + 5)
        turtle.tracer(0)

        if self.index == 31 or self.index == 32:
            self.message = '  '+self.message
        elif 0 <=self.index <=9 or self.index == 34:
            self.message = ' '+self.message
        elif self.index == 33 :
            self.message = ' '+self.message
        self.button.write(' '+self.message,align='left', font =('Times New Roman',16,'normal'))
    
    def checked(self):
        self.button.hideturtle()
        self.button.pencolor("white")
        self.button.fillcolor('#be254a')
        self.draw_button()
        return self.index
