import moves_to_use


def print_stats(level):
    print("level", level)
    print("health:", 68 + ((level - 1) * 2))
    print("defense:", int(40 + ((level - 2) * 1.5)))
    print("\n\n")




class Entity:
    def __init__(self, color, level, defense, attack, speed, health, moves):
        self.color = color
        self.name = color
        self.defense = defense
        self.attack = attack
        self.speed = speed
        self.health = health
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


# class Pikachu(Entity):
#     def __init__(self, color, level, defense, attack, speed):
#         super().__init__(color, level, defense, attack, speed)


# class Player(Entity):
#     def __init__(self):
#         super().__init__()
#         self.loc = [0,15]
#         self.name = 'Player'
#         self.moves = moves_to_use.moves_p

# class Enemy(Entity):
#     def __init__(self):
#         super().__init__()
#         self.name = 'Enemy'
#         self.moves = moves_to_use.moves_e

if __name__ == "__main__":
    test_level = 1
    # myguy = Entity()
    # myguy.level_up()
    # while test_level < 21:
    #     print_stats(test_level)
    #     test_level += 1

    # print(player.moves)
    
    #pikachu = Enemy('Yellow', 999, 999, 999, 999)
player_stats = Player('Red', 1, 10, 15, 68, 20, moves_to_use.moves_p)
enemy_stats = Enemy('Aqua', 1, 7, 10, 68, 35, moves_to_use.moves_e)