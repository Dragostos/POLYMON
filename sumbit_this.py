#python -m pip install -U --user pygame
import pygame as pg
import sys
import random
import math


pg.init()

screen = pg.display.set_mode((1000,600))
pg.display.set_caption("polymon")
mouseX = 0
mouseY = 0
pressed = 0
bools = 0
edges = [1,1]
current_map = False
on_white = False
on_green = False
map_loc = [0,3]
checked_switch = 0
checked_edge = False
running = True
start_menu = True
roaming = False
end_menu = False

class Entity:
    def __init__(self):
        self.color = 'black'

class Player(Entity):
    def __init__(self):
        super().__init__()
        self.loc = [0,15]
        self.name = 'Player'

player = Player()

def get_text(font_size, text, color, text_center):
    font = pg.font.SysFont("Arial", font_size)
    text = font.render(text, True, color)
    textRect = text.get_rect()
    textRect.center = (text_center)
    screen.blit(text, textRect)

def start_map():
    map = 'start_map'
    block_x = 225
    block_y = 25
    boolz = [
            'x == 7 or x == 8',
            'y >= 7',
            'player.loc[0] == 7 or player.loc[0] == 8',
            'player.loc[1] >= 7'
            ]
    for y in range(16):
            for x in range(16):
                    if (x == 7 or x == 8) and y <= 8:
                            color = 'white'
                    else:
                            color = 'green'
                            
                    pg.draw.rect(screen, color, (block_x, block_y, 25, 25))
                    block_x += 35
            block_y += 35
            block_x = 225
    
    return map, boolz

def vert_line():
    map = 'vert_line'
    block_x = 225
    block_y = 25
    boolz = ['x == 7 or x == 8',
            'player.loc[0] == 7 or player.loc[0] == 8'    
    ]
    for y in range(16):
            for x in range(16):
                    if x == 7 or x == 8:
                            color = 'white'
                    else:
                            color = 'green'
                            
                    pg.draw.rect(screen, color, (block_x, block_y, 25, 25))
                    block_x += 35
            block_y += 35
            block_x = 225
    return map, boolz

def hori_line():
    map = 'hori_line'
    block_x = 225
    block_y = 25
    boolz = [
        'y == 7 or y == 8',
        'player.loc[1] == 7 or player.loc[1] == 8'
    ]
    for y in range(16):
        for x in range(16):
            if y == 7 or y == 8:
                color = 'white'
            else:
                color = 'green'
            pg.draw.rect(screen, color, (block_x, block_y, 25, 25))
            block_x += 35
        block_y += 35
        block_x = 225
    return map, boolz

def cross():
    map = 'cross'
    block_x = 225
    block_y = 25
    boolz = [
        'x == 7 or x == 8',
        'y == 7 or y == 8',
        'player.loc[0] == 7 or player.loc[0] == 8',
        'player.loc[1] == 7 or player.loc[1] == 8'
    ]
    for y in range(16):
        for x in range(16):
            if (x == 7 or x == 8) or (y == 7 or y == 8):
                color = 'white'
            else:
                color = 'green'
            pg.draw.rect(screen, color, (block_x, block_y, 25, 25))
            block_x += 35
        block_y += 35
        block_x = 225
    return map, boolz

def corner(direction):
    map = 'corner'
    defined = []
    if direction == 'down right': # if (most x) and ( y == top or y == bottom) or (x == left or x == right) and (up or down)
        boolz = [
            'x >= 7',
            'y > 8',
            'player.loc[0] >= 7',
            'player.loc[1] > 8'
            ]
    elif direction == 'down left':
        boolz = [
            'x <= 8',
            'y > 8',
            'player.loc[0] <= 8',
            'player.loc[1] > 8'
            ]
    elif direction == 'up right':
        boolz = [
            'x >= 7', 
            'y < 8',
            'player.loc[0] >= 7',
            'player.loc[1] < 8'
            ]
    elif direction == 'up left':
        boolz = [
            'x <= 8',
            'y < 8',
            'player.loc[0] <= 8',
            'player.loc[1] < 8'
            ]
    block_x = 225
    block_y = 25
    for y in range(16):
        for x in range(16):
            if eval(boolz[0]) and (y==7 or y==8) or ((x == 7 or x==8) and eval(boolz[1])):
                color = 'white'
            else:
                color = 'green'
            pg.draw.rect(screen, color, (block_x, block_y, 25, 25))
            block_x += 35
        block_y += 35
        block_x = 225
    return map, boolz

def t_map(direction):
    map = 't_map'
    if direction == 'down':
        boolz = [
            'x == 7 or x == 8',
            'y >= 7',
            'y == 7 or y == 8',
            'player.loc[0] == 7 or player.loc[0] == 8',
            'player.loc[1] >= 7',
            'player.loc[1] == 7 or player.loc[1] == 8'
        ]
    elif direction == 'right':
        boolz = [
            'y == 7 or y == 8',
            'x >= 7',
            'x == 7 or x == 8',
            'player.loc[1] == 7 or player.loc[1] == 8',
            'player.loc[0] >= 7',
            'player.loc[0] == 7 or player.loc[0] == 8'
        ]
    elif direction == 'up':
        boolz = [
            'x == 7 or x == 8',
            'y <= 7',
            'y == 7 or y == 8',
            'player.loc[0] == 7 or player.loc[0] == 8',
            'player.loc[1] <= 7',
            'player.loc[1] == 7 or player.loc[1] == 8'
        ]
    elif direction == 'left':
        boolz = [
            'y == 7 or y == 8',
            'x <= 8',
            'x == 7 or x == 8',
            'player.loc[1] == 7 or player.loc[1] == 8',
            'player.loc[0] <= 8',
            'player.loc[0] == 7 or player.loc[0] == 8'
        ]

    block_x = 225
    block_y = 25
    for y in range(16):
        for x in range(16):
            if (eval(boolz[0])) and eval(boolz[1]) or (eval(boolz[2])):
                color = 'white'
            else:
                color = 'green'
            pg.draw.rect(screen, color, (block_x, block_y, 25, 25))
            block_x += 35
        block_y += 35
        block_x = 225
    return map, boolz


map_order = [
    ["t_map('right')", 'hori_line()', "t_map('down')", "corner('down left')"],
    ["corner('up right')", 'hori_line()', "t_map('left')", 'vert_line()'],
    ["corner('down right')", "t_map('down')", "t_map('up')", "t_map('left')"],
    ['start_map()', "corner('up right')", 'hori_line()', "corner('up left')"]
]


def game_won():
    roaming = False
    end_menu = True



def check_switch():
    if (player.loc[1] == 0 and (player.loc[0] == 7 or player.loc[0] == 8)) or (player.loc[0] == 15 and (player.loc[1] == 7 or player.loc[1] == 8)) or (player.loc[1] == 15 and (player.loc[0] == 7 or player.loc[0] == 8)) or (player.loc[0] == 0 and (player.loc[1] == 7 or player.loc[1] == 8)):
        return True
    elif map_loc[0] == 0 and map_loc[1] == 0 and (player.loc[0] == 7 or player.loc[0] == 8) and player.loc[1] == 0:
        game_won()
    else:
        return False
        





while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:   
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN and roaming:
            if event.key == pg.K_w and player.loc[1] >= 1:
                player.loc[1] -= 1
            elif event.key == pg.K_a and player.loc[0] >= 1: 
                player.loc[0] -= 1
            elif event.key == pg.K_s and player.loc[1] <= 14:  #s
                player.loc[1] += 1
            elif event.key == pg.K_d and player.loc[0] <= 14:
                player.loc[0] += 1


        if event.type == pg.KEYDOWN and checked_edge:
            if event.key == pg.K_w and player.loc[1] == 0:  #w
                map_loc[1] -= 1
                player.loc[1] = 15
                
            elif event.key == pg.K_a and player.loc[0] == 0: #a
                map_loc[0] -= 1
                player.loc[0] = 15
            elif event.key == pg.K_s and player.loc[1] == 15:  #s
                map_loc[1] += 1
                player.loc[1] = 0
            elif event.key == pg.K_d and player.loc[0] == 15:   #d
                map_loc[0] += 1
                player.loc[0] = 0
            
            checked_edge = False
            

            
        
    screen.fill('black')


    '''
    Start menu
    '''
    if start_menu == True:
        get_text(50, 'Welcome to Polymon!', 'white', (500, 25))
        get_text(50, 'Press Start', 'white', (500,300))
        get_text(50, 'Red', 'red', (250,500))
        get_text(50, 'Blue', 'blue', (725,500))

        if event.type == pg.MOUSEBUTTONDOWN:
            if mouseX >= 155 and mouseX <= 344 and mouseY >= 480 and mouseY <= 520:
                player.color = 'red'
            elif mouseX >= 630 and mouseX <= 821 and mouseY >= 480 and mouseY <= 520:
                player.color = 'blue'
            elif mouseX >= 400 and mouseX <= 600 and mouseY >= 280 and mouseY <= 319:
              start_menu = False
              roaming = True


    '''
    Roaming
    '''
    if roaming == True: 
        
        current_map, bools = eval(map_order[map_loc[1]][map_loc[0]])    
        
        if on_white == True:
            checked_edge = check_switch()
        
        if current_map == 'start_map':
            if (player.loc[0] == 7 or player.loc[0] == 8) and player.loc[1] <= 8:
                on_white = True
                on_green = False
            else:
                on_white = False
                on_green = True
        elif current_map == 'vert_line':
            if player.loc[0] == 7 or player.loc[0] == 8:
                on_white = True
                on_green = False
            else:
                on_white = False 
                on_green = True
        elif current_map == 'hori_line':
            if player.loc[1] == 7 or player.loc[1] == 8:
                on_white = True
                on_green = False
            else:
                on_white = False
                on_green = True
        elif current_map == 'cross':
            if (player.loc[0]==7 or player.loc[0]==8) or (player.loc[1]==7 or player.loc[1]==8):
                on_white = True
                on_green = False
            else:
                on_white = False
                on_green = True
        elif current_map == 'corner':
            if eval(bools[2]) and (player.loc[1]==7 or player.loc[1]==8) or ((player.loc[0] == 7 or player.loc[0]==8) and eval(bools[3])):
                on_white = True
                on_green = False
            else:
                on_white = False
                on_green = True
        elif current_map == 't_map':
            if eval(bools[3]) and eval(bools[4]) or eval(bools[5]):
                on_white = True
                on_green = False
            else:
                on_white = False
                on_green = True
        

    
        pg.draw.rect(screen, player.color, (225+(35*player.loc[0]), 25+(35*player.loc[1]), 25 , 25  ) )
        
        if (map_loc[0] == 0 and map_loc[1] == -1) and (player.loc[0] == 7 or player.loc[0] == 8) and player.loc[1] == 15:
            roaming = False
            end_menu = True




    '''
    End menu
    '''
    if end_menu:
        get_text(30, "Congrats! You've explored all of Polymon. I hope you enjoyed it.", 'white', (500, 200))
    




    mousePos = pg.mouse.get_pos()
    mouseX = mousePos[0]
    mouseY = mousePos[1]
    pg.display.update()