import moves_to_use


def print_stats(level):
    print("level", level)
    print("health:", 68 + ((level - 1) * 2))
    print("defense:", int(40 + ((level - 2) * 1.5)))
    print("\n\n")




class Entity:
    def __init__(self, color, level, defense, attack, speed):
        self.color = color
        self.name = color
        self.defense = defense
        self.attack = attack
        self.speed = speed

        self.level = 1
        self.experience = 0
        # self.health = 68 + ((self.level - 1) *2)
        self.health_bar = 298
        # self.defense = 40 + math.floor(  ((self.level - 2) * 1.5)  )
        # self.attack = 45 + math.floor(  ((self.level - 2) * 1.5)   )
        # self.buff = 1
        # self.debuff = 1

    def level_up(self):
        self.level = self.level + 1


class Player(Entity):
    def __init__(self, color, level, defense, attack, speed):
        super().__init__(color, level, defense, attack, speed)


class Enemy(Entity):
    def __init(self, color, level, defense, attack, speed):
        super().__init__(color, level, defense, attack, speed)



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
    player = Player('Red', 1, 10, 15, 20)
    enemy = Enemy('Aqua', 1, 7, 10, 35)
    print(f"{player.name} is facing {enemy.name}!\nP vs E defense {player.defense}:{enemy.defense}  \nP vs E attack {player.attack}:{enemy.attack} \nP vs E speed {player.speed}:{enemy.speed}")
    player.level_up()
    print(f"{player.name} is facing {enemy.name}!\nP vs E defense {player.defense}:{enemy.defense}  \nP vs E attack {player.attack}:{enemy.attack} \nP vs E speed {player.speed}:{enemy.speed}")