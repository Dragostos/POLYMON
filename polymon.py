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
import moves_to_use


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


counter = 2
text1 = 'didnt work bozo'
text2 = "didn't work either dum dum"
e_bar_x = 536

running = True

start_menu = True
roaming = False
battle = False
battle_results = False


encounter_part1 = True
encounter_part2 = False
encounter_part3 = False
health_bar_update = False
update_stats = False
getting_damage_p = True
getting_damage_e = True

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
p_damage = 0
e_damage = 0
bar_change = 0




class Entity:
    def __init__(self):
        self.color = 'black'
        self.level = 1
        self.health = 68 + ((self.level - 1) *2)
        self.health_bar = 298
        self.defense = 40 + math.floor(  ((self.level - 2) * 1.5)  )
        self.buff = 1
        self.debuff = 1
        self.moves = moves_to_use.moves

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





def get_damage(attacker, move, opponent, color):
    attacker_damage = 0
    move_text = 'no workie'
    attacker_buff = 0
    attacker_debuff = 0
    
    if attacker.moves[move]['Name'] == 'Poly Tackle':
        attacker_damage = math.floor(((((2*attacker.level)/5 + 2)*attacker.moves[move]['Power']*(opponent.health/(opponent.defense-opponent.debuff)))/50+2))
        attacker_debuff = 0
        attacker_buff = 0
        move_text = f'{color} dealt {attacker_damage} damage!'



    elif attacker.moves[move]['Name'] == 'Square Fury':
        if random.randint(1,100) <= attacker.moves[move]['Chance']:
            attacker_damage = math.floor(((((2*attacker.level)/5 + 2)*(attacker.moves[move]['Power']*2)*opponent.health/(opponent.defense-opponent.debuff))/50+2))
        else:
            attacker_damage = math.floor(((((2*attacker.level)/5 + 2)*attacker.moves[move]['Power']*opponent.health/(opponent.defense-opponent.debuff))/50+2))
        attacker_buff = 0
        attacker_debuff = 0
        move_text = f'{color} dealt {attacker_damage} damage!' 


    elif attacker.moves[move]['Name'] == 'Polyscare':
        attacker_damage = 0
        attacker_debuff = math.floor(  opponent.defense * .15  )
        move_text = f"{color}'s defense lowered!"

    elif move == 'move 3':
        
        attacker_buff = 0
        attacker_debuff = opponent.defense * .05
        move_text = f"{color}'s defense lowered!"



    elif move == 'move 3':
        attacker_damage = 0
        attacker_debuff = opponent.defense * .10
        attacker_buff = opponent.multi + (opponent.multi * 0.5)
        move_text = f"{color}'s defense lowered and atttack increased!'"
    
    return attacker_damage, move_text, attacker_buff, attacker_debuff


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

def mini_map():
    block_x = 850
    block_y = 25
    for y in range(4):
        for x in range(4):
            if map_loc[1] == y and map_loc[0] == x:
                color = player.color
            else:
                color = 'green'
            pg.draw.rect(screen, color, (block_x, block_y, 15, 15))
            block_x += 20
        block_y += 20
        block_x = 850

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

def reset_stats():
    global e_bar_x

    player.health = 68 + ((player.level - 1) *2)
    player.health_bar = 298
    player.defense = 40 + ((player.level - 2) * 1.5)

    enemy.health = 68 + ((enemy.level - 1) *2)
    enemy.health_bar = 298
    enemy.defense = 40 + ((enemy.level - 2) * 1.5)
    e_bar_x = 536
    




while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:   
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN and roaming:  #normal moving
            if event.key == pg.K_w and player.loc[1] >= 1:
                player.loc[1] -= 1
                #print("up")
            elif event.key == pg.K_a and player.loc[0] >= 1: 
                player.loc[0] -= 1
                #print('left')
            elif event.key == pg.K_s and player.loc[1] <= 14:  #s
                player.loc[1] += 1
                #print('down')
            elif event.key == pg.K_d and player.loc[0] <= 14:
                player.loc[0] += 1
                #print('right')
        
        if event.type == pg.KEYDOWN and checked_edge: #map moving
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
            if time_passed % 10 == 0:
                encounter()
        
        if event.type == timer_event and enemy_move_choice != False and player_move_choice != False:
            counter -= 1
            
      
    screen.fill('black')


    '''
    Start menu
    '''
    if start_menu == True:
        get_text(50, 'Welcome to Polymon!', 'white', (500, 25))
        if player.color == 'black':
            get_text(50, 'Select your character', 'white', (500, 300))
            get_text(50, 'Red', 'red', (250,500))
            get_text(50, 'Blue', 'blue', (725,500))
        else:
            get_text(50, 'Press Start', 'white', (500,300))
        

        if event.type == pg.MOUSEBUTTONDOWN:
            if mouseX >= 155 and mouseX <= 344 and mouseY >= 480 and mouseY <= 520:
                player.color = 'Red'
                enemy.color = 'Blue'
            elif mouseX >= 630 and mouseX <= 821 and mouseY >= 480 and mouseY <= 520:
                player.color = 'Blue'
                enemy.color = 'Red'
            elif mouseX >= 400 and mouseX <= 600 and mouseY >= 280 and mouseY <= 319:
              start_menu = False
              roaming = True


    '''
    Roaming
    '''
    if roaming == True:
        current_map, bools = eval(map_order[map_loc[1]][map_loc[0]])    
        mini_map()
        if on_white == True:
            checked_edge = check_switch()
        
        if map_loc == [0,3]:
            get_text(25, 'Use WASD keys to move your character', 'white', (500, 10))
        
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


    '''
    Encounter
    '''
    if battle:
        pg.draw.rect(screen, 'white', (100, 50, 800, 500)) #backdrop

        # if encounter_part1:# player init animation
        #     pg.draw.rect(screen, 'black', (125, 475, 750, 50))
        #     pg.draw.rect(screen, 'green', (130, 480, length_p, 40))
        #     if time_passed % 1 == 0 and length_p <= 740:
        #         length_p += 2*2
        #     get_text(40, 'Loading Player Stats', 'black', (500, 100))
        #     if length_p >= 740:
        #         encounter_part2 = True
        #         encounter_part1 = False
        # if encounter_part2: # enemy init animation
        #     pg.draw.rect(screen, 'black', (125, 475, 750, 50))
        #     pg.draw.rect(screen, 'green', (130, 480, length_e, 40))
        #     if time_passed % 1 == 0 and length_e <= 740:
        #         length_e += 2*2
        #     get_text(40, 'Loading Enemy Stats', 'black', (500, 100))
        #     if length_e >= 740:
        #         encounter_part3 = True
        #         encounter_part2 = False
        # if encounter_part3: #final animation
        #     pg.draw.rect(screen, 'black', (125, 475, 750, 50))
        #     pg.draw.rect(screen, 'green', (130, 480, length_b, 40))
        #     if time_passed % 1 == 0 and length_b <= 740:
        #         length_b += 2*2
        #     get_text(40, 'Initializing Battle', 'black', (500, 100))
        #     if length_b >= 740:
        #         get_text(40, 'Complete', 'black', (500, 300))
        #         encounter_part3 = False

        #start battle
        encounter_part1 = False
        if encounter_part1 == False and encounter_part2== False and encounter_part3 == False:
            
            pg.draw.rect(screen, 'grey', (165,55, 300, 17))  #player 
            pg.draw.rect(screen, 'green', (166, 56, player.health_bar, 15))
            pg.draw.rect(screen, player.color, (105, 55, 50,50))
            get_text(25, f'lvl {str(player.level)}', 'black', (183, 85))
            

            pg.draw.circle(screen, player_move1, (130,150), 25)
            pg.draw.circle(screen, player_move1, (230,150), 25)
            pg.draw.rect(screen, player_move1, (130, 125, 100,50))
            get_text(20, player.moves['move 1']['Name'], 'black', (180, 150))
            if mouseX >= 105 and mouseX <= 255 and mouseY >= 125 and mouseY <= 175 and player_move_choice == False:
                player_move1 = 'gold'
            elif player_move_choice == False:
                player_move1 = 'green'
            
            
            pg.draw.circle(screen, player_move2, (130,210), 25)
            pg.draw.circle(screen, player_move2, (230,210), 25)
            pg.draw.rect(screen, player_move2, (130, 185, 100,50))
            get_text(20, player.moves['move 2']['Name'], 'black', (180, 210))
            if mouseX >= 105 and mouseX <= 255 and mouseY >= 185 and mouseY <= 235 and player_move_choice == False:
                player_move2 = 'gold'
            elif player_move_choice == False:
                player_move2 = 'green'

            pg.draw.circle(screen, player_move3, (130,270), 25)
            pg.draw.circle(screen, player_move3, (230,270), 25)
            pg.draw.rect(screen, player_move3, (130, 245, 100,50))
            get_text(20, player.moves['move 3']['Name'], 'black', (180, 270))
            if mouseX >= 105 and mouseX <= 255 and mouseY >= 245 and mouseY <= 295 and player_move_choice == False:
                player_move3 = 'gold'
            elif player_move_choice == False:
                player_move3 = 'green'

            pg.draw.circle(screen, player_move4, (130,330), 25)
            pg.draw.circle(screen, player_move4, (230,330), 25)
            pg.draw.rect(screen, player_move4, (130, 305, 100,50))
            get_text(20, player.moves['move 4']['Name'], 'black', (180, 330))
            if mouseX >= 105 and mouseX <= 255 and mouseY >= 305 and mouseY <= 355 and player_move_choice == False:
                player_move4 = 'gold'
            elif player_move_choice == False:
                player_move4 = 'green'
            
            if event.type == pg.MOUSEBUTTONDOWN:
                if player_move1 == 'gold':
                    player_move1 = player.color
                    player_move_choice = 'move 1'
                elif player_move2 == 'gold':
                    player_move2 = player.color
                    player_move_choice = 'move 2'
                elif player_move3 == 'gold':
                    player_move3 = player.color
                    player_move_choice = 'move 3'
                elif player_move4 == 'gold':
                    player_move4 = player.color
                    player_move_choice = 'move 4'
                if enemy_move_choice == False:
                    enemy_move_choice = 'move 1'
                    #enemy_move_choice = 'Polyscare'
                    #enemy_move_choice = random.choice(move_options)
                
            
                




            pg.draw.rect(screen, 'grey', (535,55, 300, 17))
            pg.draw.rect(screen, 'green', (e_bar_x, 56, enemy.health_bar, 15))
            pg.draw.rect(screen, enemy.color, (845, 55, 50,50))
            get_text(25, f'lvl {str(enemy.level)}', 'black', (817, 85))
            

            pg.draw.circle(screen, enemy_move1, (870,150), 25)
            pg.draw.circle(screen, enemy_move1, (770,150), 25)
            pg.draw.rect(screen, enemy_move1, (770, 125, 100,50))
            get_text(20, enemy.moves['move 1']['Name'], 'black', (820, 150))
            
            pg.draw.circle(screen, enemy_move2, (870,210), 25)
            pg.draw.circle(screen, enemy_move2, (770,210), 25)
            pg.draw.rect(screen, enemy_move2, (770, 185, 100,50))
            get_text(20, enemy.moves['move 2']['Name'], 'black', (820, 210))

            pg.draw.circle(screen, enemy_move3, (870,270), 25)
            pg.draw.circle(screen, enemy_move3, (770,270), 25)
            pg.draw.rect(screen, enemy_move3, (770, 245, 100,50))
            get_text(20, enemy.moves['move 3']['Name'], 'black', (820, 270))

            pg.draw.circle(screen, enemy_move4, (870,330), 25)
            pg.draw.circle(screen, enemy_move4, (770,330), 25)
            pg.draw.rect(screen, enemy_move4, (770, 305, 100,50))
            get_text(20, enemy.moves['move 4']['Name'], 'black', (820, 330))

            if enemy_move_choice == enemy.moves['move 1']:
                enemy_move1 = enemy.color
            elif enemy_move_choice == enemy.moves['move 2']:
                enemy_move2 = enemy.color
            elif enemy_move_choice == enemy.moves['move 3']:
                enemy_move3 = enemy.color
            elif enemy_move_choice == enemy.moves['move 4']:
                enemy_move4 = enemy.color
            if enemy_move_choice == False:
                enemy_move1, enemy_move2, enemy_move3, enemy_move4 = 'green','green','green','green'

            if enemy_move_choice != False and player_move_choice != False:
                
                if counter == 2 and getting_damage_p == True:
                    p_damage, p_text, p_buff, p_debuff = get_damage(player, player_move_choice, enemy, player.color )
                    getting_damage_p = False
                elif counter == 0 and getting_damage_e == True:
                    e_damage, e_text, e_buff, e_debuff = get_damage(enemy, enemy_move_choice, player, enemy.color)
                    #print(e_text)
                    getting_damage_e = False
                    
               
                
                text1 = f"{player.color} used { player.moves[player_move_choice]['Name'] }!" if counter > 0 else f"{enemy.color} used { enemy.moves[enemy_move_choice]['Name'] }!"
                text2 = p_text if counter > 0 else e_text
                get_text(30, text1, 'black', (500, 450))
                get_text(30, text2, 'black', (500, 500))
                

                
                if counter == -2:
                    if player_move_choice != False and enemy_move_choice != False:
                        player.health -= e_damage 
                        enemy.health -= p_damage  
                        enemy.debuff = e_debuff
                        
                        bar_change_e = math.floor( ( enemy.health_bar * (enemy.health/(enemy.health+p_damage)) ) )
                        #print(math.floor( ( player.health_bar * (player.health/(player.health+e_damage)) ) ))
                        player.health_bar = math.floor( ( player.health_bar * (player.health/(player.health+e_damage)) ) )
                    
                    e_bar_x += enemy.health_bar - bar_change_e
                    

                    enemy.health_bar = bar_change_e



                    p_damage, e_damage = 0, 0
                    #print(moves[player_move_choice]['Name'])

                    player_move_choice = False
                    enemy_move_choice = False
                    bar_change_e, bar_change_p = 0, 0
                    getting_damage_p, getting_damage_e = True, True 
                    #player.level += 1
                    
                    counter = 2
                
                if player.health <= 0 or enemy.health <= 0:
                    battle_results = True
                    battle = False
                    encounter_part1 = True
                    encounter_part2 = False
                    encounter_part3 = False


                    
    '''
    Battle Results
    '''

    if battle_results:
        
        if player.health > 0 and enemy.health <= 0:
            player.level += 1
            enemy.level += 1

        reset_stats()

        # print(f"Player Stats\nLevel {player.level}\nHealth {player.health}\nDefense {player.defense}\n")
        # print(f"Enemy Stats\nLevel {enemy.level}\nHealth {enemy.health}\nDefense {enemy.defense}")
        # print(f"\nTheoretical damage of poly tackle (player) {math.floor(((((2*player.level)/5 + 2)*player.moves['move 2']['Power']*(enemy.health/enemy.defense))/50+2))}")
        battle_results = False
        roaming = True


    '''
    End menu
    '''
    
    




    mousePos = pg.mouse.get_pos()
    mouseX = mousePos[0]
    mouseY = mousePos[1]
    #get_text(20, f'{mouseX}, {mouseY}', 'grey', (mouseX, mouseY))
    #get_text(20, f'{str(player.defense)}, {str(enemy.defense)}', 'white', (40, 10))
    #get_text(20, f'{str(player.health)}, {str(enemy.health)}', 'white', (40, 30))
    get_text(20, f'{player.level}, {player.defense}, {player.health}', 'white', (50, 10))

    #get_text(20, f'{enemy.health}, {p_damage}, {enemy.health_bar}, {e_bar_x}, {bar_change}',  player.color,(70, 10))
    # get_text(20, f'{player.loc[0]}, {player.loc[1]}', 'white', (50, 50))
    # get_text(20, f'{map_loc[0]}, {map_loc[1]}', 'white', (50, 70))
    # get_text(20, str(time_passed), 'white', (50, 90))
    pg.display.update()