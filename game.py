import os
import keyboard
from time import sleep
from rich.panel import Panel
from rich import print

os.chdir(r'C:\Users\howar\Documents\PYTHON\MAP MOVER GAME')

with open('MAP1.txt') as file:
    map_raw = file.read()
    

map = []

for line in map_raw.split('\n'):
    row = []
    for char in line:
        row.append(char)
    map.append(row)


VIEW_SIZE = (8,20) # 6 ROWS, 10 COLUMNS

start_pos = (5,5)
current_pos = [p for p in start_pos]

def construct_mini_map(start_x, start_y):
    map_section = []
    for row in map[start_x:start_x + VIEW_SIZE[0]]:
        section_row = []
        for char in row[start_y: start_y + VIEW_SIZE[1]]:
            section_row.append(char)
        map_section.append(section_row)
    
    return map_section

def draw_map_section(mini_map):
    map_str = ""
    for row in mini_map:
        row_str = "".join(row) + "\n"
        map_str = map_str + row_str
    
    print(Panel.fit(map_str))
    print(current_pos)

# def get_move():
    # while True:
        # move = input("move?: ").upper()
        # if move == "W":
            # current_pos[0] -= 1
            # return
        # elif move == "S":
            # current_pos[0] += 1
            # return
        # elif move == "A":
            # current_pos[1] -= 2
            # return
        # elif move == "D":
            # current_pos[1] += 2
            # return
        # else:
            # print("invalid move!")

def get_keyboard():
    while True:
        move = keyboard.read_key().upper()[0]
        if move == "W":
            current_pos[0] -= 1
            sleep(0.25)
            return
        elif move == "S":
            current_pos[0] += 1
            sleep(0.25)
            return
        elif move == "A":
            current_pos[1] -= 2
            sleep(0.25)
            return
        elif move == "D":
            current_pos[1] += 2
            sleep(0.25)
            return
        elif move == "Q":
            os.system('cls')
            print('quitting now. bye!')
            quit()
        else:
            print("invalid move!")
            sleep(0.25)

def main():
    while True:
        try:
            os.system('cls')
            mini_map = construct_mini_map(current_pos[0], current_pos[1])
            draw_map_section(mini_map)
            get_keyboard()
        except KeyboardInterrupt:
            os.system('cls')
            print("all done now.  bye!")

if __name__ == "__main__":
    main()
        
        
    