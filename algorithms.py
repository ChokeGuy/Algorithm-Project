from collections import deque
import turtle
import time
import data
def BFSearch(start_x,start_y,end_x,end_y, path):
    x, y = start_x, start_y
    visited = set()
    frontier = deque()
    solution = {}
    frontier.append((x, y))
    solution[x,y] = x,y
    #white = White()
    while len(frontier) > 0:          # thoát ra khỏi vòng lập khi frontier queue bằng 0
        x, y = frontier.popleft()     # thêm vị trí x, y vào frontier 

        if(x - 25, y) in path and (x - 25, y) not in visited:  # kiểm tra ô bên trái
            cellleft = (x - 25, y)
            solution[cellleft] = x, y    # backtracking . x, y là ô hiện tại
            frontier.append(cellleft)   # thêm vào frontier list
            visited.add((x-25, y))  # thêm vào visited list

        if (x, y - 25) in path and (x, y - 25) not in visited:  # kiểm tra ô dưới
            celldown = (x, y - 25)
            solution[celldown] = x, y
            frontier.append(celldown)
            visited.add((x, y - 25))

        if(x + 25, y) in path and (x + 25, y) not in visited:   # kiểm tra ô phải
            cellright = (x + 25, y)
            solution[cellright] = x, y
            frontier.append(cellright)
            visited.add((x +25, y))

        if(x, y + 25) in path and (x, y + 25) not in visited:  # kiểm tra ô trên
            cellup = (x, y + 25)
            solution[cellup] = x, y
            frontier.append(cellup)
            visited.add((x, y + 25))
        if (x,y) != (start_x,start_y): # kiểm tra x,y có phải điểm bắt đầu không
            if (x,y) != (end_x,end_y): # kiểm tra x,y có phải điểm cuối không
                data.white.goto(x,y)
                data.white.stamp()
                turtle.tracer(4)
            else:
                break
    return solution

def DFSearch(start_x,start_y,end_x,end_y, path):
    x, y = start_x, start_y
    visited = []
    frontier = deque()
    solution = {}
    #white = White()
    frontier.append((x, y))                            # thêm x,y vào frontier list
    solution[x, y] = x, y                              # thêm x, y solution dictionary
    while len(frontier) > 0:                           # thoát ra khỏi vòng lập khi frontier queue bằng 0
        current = (x,y)                                # gắn current bằng ô hiện tại x,y
        if(x - 25, y) in path and (x - 25, y) not in visited:  # check left
            cellleft = (x - 25, y)
            solution[cellleft] = x, y  # backtracking . x, y là ô hiện tại
            frontier.append(cellleft)  # thêm vào frontier list

        if (x, y - 25) in path and (x, y - 25) not in visited:  # check down
            celldown = (x, y - 25)
            solution[celldown] = x, y  
            frontier.append(celldown)

        if(x + 25, y) in path and (x + 25, y) not in visited:   # check right
            cellright = (x + 25, y)
            solution[cellright] = x, y  
            frontier.append(cellright)

        if(x, y + 25) in path and (x, y + 25) not in visited:  # check up
            cellup = (x, y + 25)
            solution[cellup] = x, y  
            frontier.append(cellup)

        x, y = frontier.pop()           # xóa x,y ra khỏi frontier
        visited.append(current)         # thêm current vào visited list
        if (x,y) != (start_x,start_y):
            if (x,y) != (end_x,end_y):
                data.white.goto(x,y)
                data.white.stamp()
                turtle.tracer(4)
            else:
                break
    return solution

