import os
import numpy as np

'''LAY DUONG DAN DEN FOLDER MAPS'''
path_board = os.getcwd() + '\\maps'

'''LAY HET TAT CA CAC MAP, PLAYER, TREASER BO VAO TUNG LIST'''
def get_maps():
    os.chdir(path_board)
    list_maps = []
    list_player = []
    list_treasure = []
    for file in os.listdir():
        if file.endswith(".txt"):
            file_path = f"{path_board}\{file}"
            board, player, treasure = get_map(file_path)
            list_maps.append(board)
            list_player.append(player)
            list_treasure.append(treasure)
    return list_maps, list_player, list_treasure

'''TIM PLAYER, TREASER TREN TUNG MAP'''
def find_player_treasure(result):
    width = len(result[0])
    height = len(result)
    for i in range(height):
        for j in range(width):
            if(result[i][j] == 'P'):
                player = [i, j]
                result[i][j] = ' '
            elif(result[i][j] == 'T'):
                treasure = [i, j]
                result[i][j] = ' '
    return player, treasure

''' DOC TUNG FILE TXT '''
def get_map(path):
    result = np.loadtxt(f"{path}", dtype=str, delimiter=',')
    player, treasure = find_player_treasure(result)
    return result, player, treasure

def get_setting_up_maze():
    os.chdir(path_board)
    levels = []
    for file in os.listdir():
        if file.endswith(".txt"):
            file_path = f"{path_board}\{file}"
            grid = []
            with open(file_path) as file:
                for line in file:
                    grid.append(line.replace(",", ""))
            levels.append(grid)
    return levels