'''
To-Do
- move some of the code from the create task to this file which makes the start menu easier to understand
    Predicted diff - Low
- re-do stats with Brayden
    Predicted diff - mid-high
- IF^IS DONE: remake the damage/health bar issue
    Predicted diff - mid-high
- Make a minimap which shows where you are
    Predicted diff - low
- create a Legend (HUD)
    Predicted diff - low-mid
- Try to move code around to make it a little simpler/easier to understand
    predicted diff - mid-high

'''
#python -m pip install -U --user pygame
import pygame as pg
import sys
import random
import math


pg.init()

screen = pg.display.set_mode((1000,600))
pg.display.set_caption("deez nuts")
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


time_delay = 1000
timer_event = pg.USEREVENT + 1
pg.time.set_timer(timer_event, time_delay)
time_passed = 0
length_p = 1
length_e = 1
length_b = 1


counter = 4
text1 = 'didnt work bozo'
text2 = "didn't work either dum dum"
e_bar_x = 536



running = True

start_menu = True
roaming = False
battle = False
battle_finish = False


encounter_part1 = True
encounter_part2 = False
encounter_part3 = False
health_bar_update = False
update_stats = False

player_move1 = 'green'
player_move2 = 'green'
player_move3 = 'green'
player_move4 = 'green'

enemy_move1 = 'green'
enemy_move2 = 'green'
enemy_move3 = 'green'
enemy_move4 = 'green'

player_move_choice = False
enemy_move_choice = False

move_stats = {
    'Square Fury' : {
        'Damage': 2
    },
    'Arrow Storm': {
        'Chance': 5,
        'Damage': 2
    },
    'Polyscare': {
        'Debuff': 1.5
    },
    'Ridicule': {
        'Attack Buff Increase': 1.5,
        'Defense Debuff Decrease': 1.5
    }
}

move_options = ['Square Fury', 'Arrow Storm', 'Polyscare', 'Ridicule']


def damage(attacker, move, opponent):
    if move == 'Square Fury':
        damage = attacker.move_stats[move]['Damage']  +   math.floor(attacker.move_stats[move]['Damage'] * attacker.multi)
        if attacker.buff != 1:
            damage *= player.buff
        debuff = 0
        buff = 0
        move_text = f'{attacker.name} dealt {damage} damage!'



    elif move == 'Arrow Storm':
        damage = attacker.multi*(attacker.move_stats[move]['Damage']  +   math.floor(attacker.move_stats[move]['Damage'] * attacker.multi)) if random.randint(1,100) <= 5 else attacker.move_stats[move]['Damage']  +   math.floor(attacker.move_stats[move]['Damage'] * attacker.multi)
        if attacker.buff != 1:
            damage *= player.buff
        buff = 0
        debuff = 0
        move_text = f'{attacker.name} dealt {damage} damage!'

    elif move == 'Polyscare':
        damage = 0
        buff = 0
        debuff = opponent.defense * .05
        move_text = f"{opponent.name}'s defense lowered!"

    elif move == 'Ridicule':
        damage = 0
        debuff = opponent.defense * .10
        buff = opponent.multi + (opponent.multi * 0.5)
        move_text = f"{opponent.name}'s defense lowered and atttack increased!'"
    
    return damage, move_text, buff, debuff



class Entity:
    def __init__(self):
        self.color = 'black'
        self.level = 1
        self.multi = self.level * 1.5
        self.health = 68
        self.health_bar = 298
        self.defense = 40
        self.buff = 1
        self.debuff = 1
        self.move_stats = move_stats

class Player(Entity):
    def __init__(self):
        super().__init__()
        self.loc = [0,15]
        self.name = 'Player'

class Enemy(Entity):
    def __init__(self):
        super().__init__()
        self.name = 'Enemy'

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


map_order = [
    ["corner('down right')", 'hori_line()', "t_map('down')", "corner('down left')"],
    ["corner('up right')", 'hori_line()', "t_map('left')", 'vert_line()'],
    ["corner('down right')", "t_map('down')", "t_map('up')", "t_map('left')"],
    ['start_map()', "corner('up right')", 'hori_line()', "corner('up left')"]
]


def check_switch():
    if (player.loc[1] == 0 and (player.loc[0] == 7 or player.loc[0] == 8)) or (player.loc[0] == 15 and (player.loc[1] == 7 or player.loc[1] == 8)) or (player.loc[1] == 15 and (player.loc[0] == 7 or player.loc[0] == 8)) or (player.loc[0] == 0 and (player.loc[1] == 7 or player.loc[1] == 8)):
        return True
    else:
        return False
        
def encounter():
    global roaming, battle
    roaming = False
    battle = True






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
            

        if event.type == timer_event and on_green == True:  # encounter
            time_passed += 1
            if time_passed % 1 == 0:
                encounter()
            else:
                print("hello")
        
        if event.type == timer_event and enemy_move_choice != False and player_move_choice != False:
            counter -= 1
            
            
            
        
    screen.fill('black')


    '''
    Start menu
    '''
    if start_menu == True:
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
        

        
        # get_text(20, f'White: {on_white}', 'white', (900, 10))
        # get_text(20, f'Green: {on_green}', 'green', (900, 30))
        # get_text(20, f'Edge: {checked_edge}', 'white', (900, 50))
        # get_text(20, current_map, 'red', (900, 70))
        # get_text(20, map_order[map_loc[1]][map_loc[0]], 'red', (900, 90))
        
        
        pg.draw.rect(screen, player.color, (225+(35*player.loc[0]), 25+(35*player.loc[1]), 25 , 25  ) )


    '''
    Encounter
    '''
    if battle:
        pg.draw.rect(screen, 'white', (100, 50, 800, 500)) #backdrop

        if encounter_part1:# player init animation
            pg.draw.rect(screen, 'black', (125, 475, 750, 50))
            pg.draw.rect(screen, 'green', (130, 480, length_p, 40))
            if time_passed % 1 == 0 and length_p <= 740:
                length_p += 2*2
            get_text(40, 'Loading Player Stats', 'black', (500, 100))
            if length_p >= 740:
                encounter_part2 = True
                encounter_part1 = False
        if encounter_part2: # enemy init animation
            pg.draw.rect(screen, 'black', (125, 475, 750, 50))
            pg.draw.rect(screen, 'green', (130, 480, length_e, 40))
            if time_passed % 1 == 0 and length_e <= 740:
                length_e += 2*2
            get_text(40, 'Loading Enemy Stats', 'black', (500, 100))
            if length_e >= 740:
                encounter_part3 = True
                encounter_part2 = False
        if encounter_part3: #final animation
            pg.draw.rect(screen, 'black', (125, 475, 750, 50))
            pg.draw.rect(screen, 'green', (130, 480, length_b, 40))
            if time_passed % 1 == 0 and length_b <= 740:
                length_b += 2*2
            get_text(40, 'Initializing Battle', 'black', (500, 100))
            if length_b >= 740:
                get_text(40, 'Complete', 'black', (500, 300))
                encounter_part3 = False


        #start battle

        if encounter_part1 == False and encounter_part2== False and encounter_part3 == False:
            

            #get_text(20, 'I', 'black', (500, 50)) #middle
            
            
            
            pg.draw.rect(screen, 'grey', (165,55, 300, 17))  #player 
            pg.draw.rect(screen, 'green', (166, 56, player.health_bar, 15))
            pg.draw.rect(screen, player.color, (105, 55, 50,50))
            get_text(25, f'lvl {str(player.level)}', 'black', (183, 85))
            

            pg.draw.circle(screen, player_move1, (130,150), 25)
            pg.draw.circle(screen, player_move1, (230,150), 25)
            pg.draw.rect(screen, player_move1, (130, 125, 100,50))
            get_text(20, "Square Fury", 'black', (180, 150))
            if mouseX >= 105 and mouseX <= 255 and mouseY >= 125 and mouseY <= 175 and player_move_choice == False:
                player_move1 = 'gold'
            elif player_move_choice == False:
                player_move1 = 'green'
            
            
            pg.draw.circle(screen, player_move2, (130,210), 25)
            pg.draw.circle(screen, player_move2, (230,210), 25)
            pg.draw.rect(screen, player_move2, (130, 185, 100,50))
            get_text(20, "Arrow Storm", 'black', (180, 210))
            if mouseX >= 105 and mouseX <= 255 and mouseY >= 185 and mouseY <= 235 and player_move_choice == False:
                player_move2 = 'gold'
            elif player_move_choice == False:
                player_move2 = 'green'

            pg.draw.circle(screen, player_move3, (130,270), 25)
            pg.draw.circle(screen, player_move3, (230,270), 25)
            pg.draw.rect(screen, player_move3, (130, 245, 100,50))
            get_text(20, "Polyscare", 'black', (180, 270))
            if mouseX >= 105 and mouseX <= 255 and mouseY >= 245 and mouseY <= 295 and player_move_choice == False:
                player_move3 = 'gold'
            elif player_move_choice == False:
                player_move3 = 'green'

            pg.draw.circle(screen, player_move4, (130,330), 25)
            pg.draw.circle(screen, player_move4, (230,330), 25)
            pg.draw.rect(screen, player_move4, (130, 305, 100,50))
            get_text(20, "Ridicule", 'black', (180, 330))
            if mouseX >= 105 and mouseX <= 255 and mouseY >= 305 and mouseY <= 355 and player_move_choice == False:
                player_move4 = 'gold'
            elif player_move_choice == False:
                player_move4 = 'green'
            
            if event.type == pg.MOUSEBUTTONDOWN:
                if player_move1 == 'gold':
                    player_move1 = player.color
                    player_move_choice = 'Square Fury'
                elif player_move2 == 'gold':
                    player_move2 = player.color
                    player_move_choice = 'Arrow Storm'
                elif player_move3 == 'gold':
                    player_move3 = player.color
                    player_move_choice = 'Polyscare'
                elif player_move4 == 'gold':
                    player_move4 = player.color
                    player_move_choice = 'Ridicule'
                if enemy_move_choice == False:
                    #enemy_move_choice = 'Square Fury'
                    enemy_move_choice = random.choice(move_options)
                
            
                




            pg.draw.rect(screen, 'grey', (535,55, 300, 17))
            pg.draw.rect(screen, 'green', (e_bar_x, 56, enemy.health_bar, 15))
            pg.draw.rect(screen, enemy.color, (845, 55, 50,50))
            get_text(25, f'lvl {str(enemy.level)}', 'black', (817, 85))
            

            pg.draw.circle(screen, enemy_move1, (870,150), 25)
            pg.draw.circle(screen, enemy_move1, (770,150), 25)
            pg.draw.rect(screen, enemy_move1, (770, 125, 100,50))
            get_text(20, "Square Fury", 'black', (820, 150))
            
            pg.draw.circle(screen, enemy_move2, (870,210), 25)
            pg.draw.circle(screen, enemy_move2, (770,210), 25)
            pg.draw.rect(screen, enemy_move2, (770, 185, 100,50))
            get_text(20, "Arrow Storm", 'black', (820, 210))

            pg.draw.circle(screen, enemy_move3, (870,270), 25)
            pg.draw.circle(screen, enemy_move3, (770,270), 25)
            pg.draw.rect(screen, enemy_move3, (770, 245, 100,50))
            get_text(20, "Polyscare", 'black', (820, 270))

            pg.draw.circle(screen, enemy_move4, (870,330), 25)
            pg.draw.circle(screen, enemy_move4, (770,330), 25)
            pg.draw.rect(screen, enemy_move4, (770, 305, 100,50))
            get_text(20, "Ridicule", 'black', (820, 330))

            if enemy_move_choice == move_options[0]:
                enemy_move1 = enemy.color
            elif enemy_move_choice == move_options[1]:
                enemy_move2 = enemy.color
            elif enemy_move_choice == move_options[2]:
                enemy_move3 = enemy.color
            elif enemy_move_choice == move_options[3]:
                enemy_move4 = enemy.color
            if enemy_move_choice == False:
                enemy_move1, enemy_move2, enemy_move3, enemy_move4 = 'green','green','green','green'

            if enemy_move_choice != False and player_move_choice != False:
                p_damage, p_text, p_buff, p_debuff = damage(Player(), player_move_choice, Enemy())
                e_damage, e_text, e_buff, e_debuff = damage(Enemy(), enemy_move_choice, Player())
               
                text1 = f'Player used {player_move_choice}!' if counter > 0 else f'Enemy used {enemy_move_choice}!'
                text2 = p_text if counter > 0 else e_text
                
                get_text(30, text1, 'black', (500, 250))
                get_text(30, text2, 'black', (500, 300))
                #health bar movement
                


                if health_bar_update:
                    enemy.health_bar -= (2+player.multi)*(player.health_bar/(68-p_damage))
                    player.health_bar -= (2+enemy.multi)*(enemy.health_bar/(68-e_damage))
                    health_bar_update = False

                if update_stats:
                    player.health -= e_damage
                    enemy.health -= p_damage
                    player.buff += e_buff
                    player.debuff += e_debuff
                    enemy.buff += p_buff
                    enemy.debuff += p_debuff

                    update_stats = False


                

                if counter == -4:
                    health_bar_update = True
                    update_stats = True
                    player_move_choice = False
                    enemy_move_choice = False
                    counter = 4





    '''
    End menu
    '''
    
    




    mousePos = pg.mouse.get_pos()
    mouseX = mousePos[0]
    mouseY = mousePos[1]
    #get_text(20, f'{mouseX}, {mouseY}', 'grey', (mouseX, mouseY))
    get_text(20, f'{str(player.health_bar)}, {str(enemy.health_bar)}', 'white', (500, 30))

    # get_text(20, player.color,  player.color,(50, 30))
    # get_text(20, f'{player.loc[0]}, {player.loc[1]}', 'white', (50, 50))
    # get_text(20, f'{map_loc[0]}, {map_loc[1]}', 'white', (50, 70))
    # get_text(20, str(time_passed), 'white', (50, 90))
    pg.display.update()