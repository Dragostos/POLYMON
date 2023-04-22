'''

Concept: Very simple game, its a single pokemon themed battle between a blue square and a red square. You can choose to be either square, everything is the same.

Updated Concept:
    Simple entry screen, moves to like 9 or more pre-made maps. All together, it's one big map condensed into 'chunks' in minecraft terms.
        prolly can just copy off of a pokemon map
    You encounter squares, there will be different colors. there's the starters: Blue, and Red. Theres more such as Green, Blue, Purple and Yellow.
    You can catch or defeat these squares which will level you up (max level 5); you start at level 1.
    You can have a max of three Squares at a time.

    Battles will be as follows: (will figure out who goes first later), once it's your turn after who goes first is decided then you select a choice
    Your choices are Attack, Item, and (ill figure that out later).
    Attack - You can use your moves
    Item - Capture squares or repair square.
    ??? - ???
    
    Idk how many moves i wanna make but we'll see. I could try and make a system that only requires three moves and you can upgrade these moves as you progress.
    ^ i like that system. so im gonna try and make it.


DUI idea
    Legend
    Goals

Combat
    Moves
        Square fury
            Is just tackle.
            Improvements: increases damage
        Arrow storm 
            shoots arrows, has a chance to attack again
            Improvements: higher chance of attacking again OR more damage
        Polyscare
            debuffs the opponents attack or defense (chosen at the beginning)
            Improvements: increases the debuff
        Ridicule
            Boosts opponents attack but lowers their defense
            Improvements: lowers the attack buff OR increases the defense debuff
    Items
        Capture device
            captures wild sqaures
        Repair Square
            heals


'''
#python -m pip install -U --user pygame
import pygame as pg
import sys
import random

pg.init()

screen = pg.display.set_mode((1000,600))
pg.display.set_caption("deez nuts")
mouseX = 0
mouseY = 0
basic_menu = True
attack_menu = False
pressed = 0



current_map = False
on_white = False
on_green = False
map_loc = [0,3]
checked_switch = 0
checked_edge = False


time_delay = 1000
timer_event = pg.USEREVENT + 1
pg.time.set_timer(timer_event, time_delay)
time_passed = 0
restart = False


running = True
part1 = True
part2 = False
part3 = False


move_stats = {
    'Square Fury' : {
        'Damage': 1
    },
    'Arrow Storm': {
        'Chance': 1,
        'Damage': 1
    },
    'Polyscare': {
        'Damage': 1
    },
    'Ridicule': {
        'Attack Buff Decrease': 1,
        'Defense Debuff Increase': 1
    }
}

class Entity:
    def __init__(self):
        self.color = 'black'
        self.level = 1
        self.health = 68
        self.defense = 40
        self.move_stats = move_stats

class Player(Entity):
    def __init__(self):
        super().__init__()
        self.loc = [0,15]

class Enemy(Entity):
    def __init__(self):
        super().__init__()
        self.move_stats = move_stats

player = Player()
enemy = Enemy()

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
bools = 0

map_order = [
    ["corner('down right')", 'hori_line()', "t_map('down')", "corner('down left')"],
    ["corner('up right')", 'hori_line()', "t_map('left')", 'vert_line()'],
    ["corner('down right')", "t_map('down')", "t_map('up')", "t_map('left')"],
    ['start_map()', "corner('up right')", 'hori_line()', "corner('up left')"]
]
#checked_edge = False
edges = [1,1]

def check_switch():
    if (player.loc[1] == 0 and (player.loc[0] == 7 or player.loc[0] == 8)) or (player.loc[0] == 15 and (player.loc[1] == 7 or player.loc[1] == 8)) or (player.loc[1] == 15 and (player.loc[0] == 7 or player.loc[0] == 8)) or (player.loc[0] == 0 and (player.loc[1] == 7 or player.loc[1] == 8)):
        return True
    else:
        return False
        
def encounter():
    global part2, part3
    part2 = False
    part3 = True

    


while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:   
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN and part2:
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
            

        if event.type == timer_event and on_green == True:  #enemy spawning
            time_passed += 1
            if time_passed % 1 == 0:
                encounter()
            else:
                print("hello")
            #make a variable count, and stay for however long using mod that number, i.e time_passed%3 to stay for three seconds
            
            
        
    screen.fill('black')


    '''
    Start menu
    '''
    if part1 == True:
        get_text(50, 'Welcome to Polymon!', 'white', (500, 25))
        get_text(50, 'Press Start', 'white', (500,300))
        get_text(50, 'Team Red', 'red', (250,500))
        get_text(50, 'Team Blue', 'blue', (725,500))
        


        if event.type == pg.MOUSEBUTTONDOWN:
            if mouseX >= 155 and mouseX <= 344 and mouseY >= 480 and mouseY <= 520:
                player.color = 'red'
                enemy.color = 'blue'
            elif mouseX >= 630 and mouseX <= 821 and mouseY >= 480 and mouseY <= 520:
                player.color = 'blue'
                enemy.color = 'red'
            elif mouseX >= 400 and mouseX <= 600 and mouseY >= 280 and mouseY <= 319:
              part1 = False
              part2 = True


    '''
    Roaming
    '''
    if part2 == True: 
        
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
        

        
        get_text(20, f'White: {on_white}', 'white', (900, 10))
        get_text(20, f'Green: {on_green}', 'green', (900, 30))
        get_text(20, f'Edge: {checked_edge}', 'white', (900, 50))
        get_text(20, current_map, 'red', (900, 70))
        get_text(20, map_order[map_loc[1]][map_loc[0]], 'red', (900, 90))
        
        
        pg.draw.rect(screen, player.color, (225+(35*player.loc[0]), 25+(35*player.loc[1]), 25 , 25  ) )


    '''
    Battle
    '''
    if part3 == True:
        pg.draw.rect(screen, 'white', (100, 50, 800, 500)) #backdrop

        pg.draw.rect(screen , player.color, (150, 450, 50,50))
        




    '''
    End menu
    '''
    
    




    mousePos = pg.mouse.get_pos()
    mouseX = mousePos[0]
    mouseY = mousePos[1]
    get_text(20, f'{mouseX}, {mouseY}', 'white', (50, 10))
    get_text(20, player.color,  player.color,(50, 30))
    get_text(20, f'{player.loc[0]}, {player.loc[1]}', 'white', (50, 50))
    get_text(20, f'{map_loc[0]}, {map_loc[1]}', 'white', (50, 70))
    get_text(20, str(time_passed), 'white', (50, 90))
    pg.display.update()