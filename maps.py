import pygame as pg
screen = pg.display.set_mode((1000,600))
map_loc = [0,3]

def start_map():
    map = 'start_map'
    block_x = 225
    block_y = 25
    boolz = [
            'x == 7 or x == 8',
            'y <= 8',
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
    defined = []# if (most x) and ( y == top or y == bottom) or (x == left or x == right) and (up or down)
    if direction == 'down right': 
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

