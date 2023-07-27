import moves_to_use
import math
import random

def print_stats(user):
    print("level", user.level)
    print("defense:", user.defense)
    print("attack:", user.attack)
    print("speed:", user.speed)
    print("health:", user.health)
    
    
    print("\n\n")


#make the entry stats on a 1-10 scale

#defense 
class Entity:
    def __init__(self, color, level, defense, attack, speed, health, moves):
        #print(defense, attack, speed, health)
        self.color = color
        self.name = color
        self.defense = 40 + math.floor( math.pow(defense, 1.5)  )
        self.attack = 80 + math.floor( math.pow(attack, 1.5)  )
        self.speed = 20 + math.floor( math.pow(speed, 1.5)  )
        self.health = 60 + math.floor( math.pow(health, 1.5)  )
        self.moves = moves
        self.level = level
        self.experience = 0
        self.health_bar = 298
        self.crit_chance = 35


    def level_up(self):
        self.level = self.level + 1
        self.defense += 4
        self.attack += 4
        self.speed += 2
        self.health += 10


class Player(Entity):
    def __init__(self, color, level, defense, attack, speed, health, moves):
        super().__init__(color, level, defense, attack, speed, health, moves)
        self.loc = [0,15]


class Enemy(Entity):
    def __init__(self, color, level, defense, attack, speed, health, moves):
        super().__init__(color, level, defense, attack, speed, health, moves)


if __name__ == "__main__":
    test_level = 1
    # myguy = Entity()
    # myguy.level_up()
    # while test_level < 21:
    #     print_stats(test_level)
    #     test_level += 1

    # print(player.moves)
    
    #pikachu = Enemy('Yellow', 999, 999, 999, 999)
player_stats = Player('Red', 1, 1, 1, 1, 1, moves_to_use.moves_p)
#print_stats(player_stats)
enemy_stats = Enemy('Aqua', 1, 7, 10, 68, 35, moves_to_use.moves_e)


def test_stats():
    class poopy(Entity):
        def __init__(self, color, level, defense, attack, speed, health, moves):
            super().__init__(color, level, defense, attack, speed, health, moves)
    poopy_butt1 = poopy('Blue', 1, 1, 1, 1, 1, moves_to_use.moves_p)
    lvl = 50
    poopy_butt2 = poopy('Blue', lvl, lvl, lvl, lvl, lvl, moves_to_use.moves_p)
    
    print_stats(poopy_butt1)
    print_stats(poopy_butt2)
    
    # for i in range(100):
        
    #     #print('level', str(i+1))
    #     print_stats(poopy_butt)

test_stats()