from objects import *
import turtle
import buttons
import data
import get_maps as gm
from algorithms import *
import sys
import time

map_number = 0
def btnclick(x,y):
    global map_number
    for button in data.buttons:
        x_cor,y_cor,length,width,index = button 
        if x_cor < x <= x_cor + length and y_cor < y <= y_cor + width:  
                map_number = index -1         
                get_map(map_number)
                turtle.tracer(0)
                break
            
    if -510 <= x <= -440:
        if 140 <= y < 175:
            get_map(map_number)
            start_time = time.time()  
            solution = DFSearch(start_x,start_y,end_x,end_y, path)
            end_time = time.time()
            game.backRoute(start_x,start_y,end_x, end_y, solution)    
            t1=round(end_time - start_time, 2)  #tính thời gian thực thi thuật toán
            timeDFS = Button(-240, 350, 50, 30, str(t1) + 's', 41)
            timeDFS.draw_button()                 

        if 60 <= y < 95:
            get_map(map_number)
            start_time = time.time()
            solution = BFSearch(start_x,start_y,end_x,end_y, path)
            end_time = time.time()
            game.backRoute(start_x,start_y,end_x, end_y, solution) 
            t2=round(end_time - start_time, 2)  #tính thời gian thực thi thuật toán
            timeBFS = Button(-240, 350, 50, 30, str(t2) + 's', 43)
            timeBFS.draw_button()

        if -20 <= y < 15:
            game.state = False
            sys.exit()

def get_map(map_number):
    game.reset_map()
    game.setup_maze(levels[map_number])
    buttons.draw_table_of_levels()
    buttons.draw_menu_option()

class Game():    
    def __init__(self):
        self.screen= turtle.Screen()
        self.screen.bgpic("./images/bgd.gif")
        self.screen.title("Maze Game")
        self.screen.setup(1200, 800)
        self.button_checked = True
        self.screen.register_shape("./images/bgd.gif")
        self.screen.register_shape("./images/wall.gif")
        self.screen.register_shape("./images/player.gif")
        self.screen.register_shape("./images/treasure.gif")
        self.screen.register_shape("./images/walk.gif")
        self.state = True
        self.treasures = []
        self.walls = []
        self.player = Player(self.walls)
        self.pen = Pen()   
        self.walk = Walk()    
        self.screen.onclick(btnclick,1)

    def reset_map(self):
        self.pen.clearstamps()
        self.walk.clearstamps()
        data.white.clearstamps()
        self.pen.hideturtle()
        self.player.hideturtle()
        self.treasure.hideturtle()     
        self.button_checked = True
        self.screen.title("Maze Game")
        self.treasures = []
        self.walls = []
        self.player = Player(self.walls)
        self.pen = Pen()
        self.walk = Walk()
        data.white = White()

    def backRoute(self, start_x,start_y, x, y, solution):
        self.walk.goto(solution[x, y])
        self.walk.stamp()
        steps = 0 
        #dừng lại khi về tới vị trí bắt đầu (x,y) == (start_x, start_y)
        while solution[x,y] != solution[start_x, start_y]:  
            self.walk.goto(solution[x, y])      #tô  màu cho đường đi  
            self.walk.stamp()
            turtle.tracer(0) 
            x,y = solution[x, y] 
            steps += 1
            len = Button(-210, 310, 50, 30, str(steps), 40)
            len.draw_button()

    def setup_maze(self,level):
        global start_x, start_y, end_x, end_y, path
        path =[]
        for y in range(len(level)):
            for x in range(len(level[y])):
                #get the character at each x, y coordinate
                #note the order of y and x in the next line
                character = level[y][x] #x appears after y
                #calculate the screen x, y coordinate
                screen_x = -340 + (x * 25)
                screen_y = 288 - (y * 25)
                #check if it is an X (representing a wall)
                if character == "X":
                    self.pen.goto(screen_x, screen_y)
                    self.pen.stamp()
                    #add coordinates to wall list 
                    self.walls.append((screen_x, screen_y))
                if character == " " or character == "T":
                    path.append((screen_x, screen_y))  
                #check if it is a P (representing the player)
                if character == "P":
                    self.player.goto(screen_x, screen_y)
                    start_x, start_y = screen_x, screen_y 
                #check if it is a T (reprensenting Treasure)
                if character == "T":
                    end_x, end_y = screen_x,screen_y 
                    self.treasure = Treasure(screen_x, screen_y)
                    self.treasures.append(self.treasure)
                turtle.tracer(0)
        self.screen.update()
    
    def mainloop(self):
        turtle.tracer(0)
        #main game loop
        while self.state == True:
            self.screen.update()

if __name__ == "__main__":
    game = Game()
    levels = []
    levels = gm.get_setting_up_maze()

    game.setup_maze(levels[0])
    buttons.draw_table_of_levels()
    buttons.draw_menu_option()

    game.mainloop()