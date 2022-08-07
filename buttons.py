from objects import Button
import data

#options
def draw_menu_option():
    btn_DFS = Button(-510, 140, 80, 35, 'DFS',31)
    btn_DFS.draw_button()
    btn_BFS = Button(-510,60,80, 35, 'BFS',32)
    btn_BFS.draw_button()
    btn_quit = Button(-510, -20, 80, 35, 'QUIT',33)
    btn_quit.draw_button()

    #algorithms information
    btn_time = Button(-300, 350, 160, 30, 'Time: ',35)
    btn_time.draw_button()
    btn_len = Button(-300, 310, 160, 30, 'Length: ',36)
    btn_len.draw_button()

def draw_table_of_levels():
    btn_title = Button(400 ,300, 100, 40, 'MAPS',34)
    btn_title.draw_button()
    index = 1
    xcor = 350
    ycor = 250
    #table of levels
    for i in range(5):
        for j in range(4):
            global btn_levels        
            btn_levels = Button(xcor, ycor, 40, 40,f'{index}',index)#,get_map
            data.buttons.append([btn_levels.button_x,btn_levels.button_y,btn_levels.buttonLength,btn_levels.buttonWidth,index])
            btn_levels.draw_button()          
            xcor += 50
            index += 1
        ycor -= 50
        xcor = 350