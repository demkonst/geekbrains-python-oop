from random import choice, randint


class Hamster:
    id = 0
    position = [0, 0]
    health = 0

    def __init__(self, id, map):
        self.id = id
        self.health = randint(1, 3)
        self.position = self.get_clear_position(map)

    def get_clear_position(self, map):
        map_height = len(map.split('\n'))
        map_width = len(map.split('\n')[0])
        while True:
            pos = [randint(0, map_width-1), randint(0, map_height-1)]
            if map.split('\n')[pos[1]][pos[0]] == '*':
                return pos

    def on_shot(self):
        self.health -= 1
        return self.health == 0
