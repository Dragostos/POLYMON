import moves_to_use


def print_stats(level):
    print("level", level)
    print("health:", 68 + ((level - 1) * 2))
    print("defense:", int(40 + ((level - 2) * 1.5)))
    print("\n\n")


if __name__ == "__main__":
    test_level = 1
    while test_level < 21:
        print_stats(test_level)
        test_level += 1


class Entity:
    def __init__(self):
        self.color = 'black'
        self.level = 1
        self.experience = 0
        self.health = 68 + ((self.level - 1) *2)
        self.health_bar = 298
        self.defense = 40 + math.floor(  ((self.level - 2) * 1.5)  )
        self.attack = 45 + math.floor(  ((self.level - 2) * 1.5)   )
        self.buff = 1
        self.debuff = 1


class Red(Entity):
    def __init__(self):
        self.name = 'Red'


class Blue(Entity):
    def __init__(self):
        self.name = 'Blue'

class Purple(Entity):
    def __init__(self):
        self.name = 'Purple'
        


class Player(Entity):
    def __init__(self):
        super().__init__()
        self.loc = [0,15]
        self.name = 'Player'
        self.moves = moves_to_use.moves_p

class Enemy(Entity):
    def __init__(self):
        super().__init__()
        self.name = 'Enemy'
        self.moves = moves_to_use.moves_e


