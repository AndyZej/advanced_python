def attack():
    pass

def move():
    pass

MAP_SIZE = 50

enemy = {
    'name': '',
    'health': 100,
    "strength": 100,
    "dexterity": 100,
    "constitution": 100,
    "attack": attack,
    "move": move
}

enemy2 = {
    'name': '',
    'health': 100,
    "strength": 100,
    "constitution": 100,
    "attack": attack,
    "move": move
}

player = {
    'name': '',
    'health': 100,
    "strength": 100,
    "attack": attack,
}

enemies = [enemy, enemy2]

print(type(enemy2))
print(type(player))


def save():
    pass


a = attack



class Player:
    def __init__(self, name, health, strength, dexterity, constitution):
        self.name = name
        self.health = health
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution

    def attack(self):
        pass


class Enemy:
    def __init__(self, name, health, strength, dexterity, constitution):
        self.name = name
        self.health = health
        self.strength = strength


p = Player(player['name'], 100, 100, 100, 100)
p2 = Player(player['name'], 100, 100, 100, 100)
e = Enemy(player['name'], 100, 100, 100, 100)

print(type(e))
print(type(p))