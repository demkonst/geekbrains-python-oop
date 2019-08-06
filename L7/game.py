from player import Player
from hamster import Hamster


class Game:
    map = """****\n****\n****\n****"""
    happy_message = 'You won!'
    hamsters_count = 3
    back = {'w': 's', 'a': 'd', 's': 'w', 'd': 'a'}

    player = Player()
    hamsters = []
    gameon = False

    def __init__(self):
        for i in range(self.hamsters_count):
            full_map = self.get_full_map(self.map)

            self.hamsters.append(
                Hamster(i+1, full_map))

    def add_point(self, position, name, map):
        li = map.split('\n')
        row = li[position[1]]
        row = row[:position[0]]+name+row[position[0]+1:]
        li[position[1]] = row
        return '\n'.join(li)

    def render_map(self):
        s = self.get_full_map(self.map)
        print(s)

    def get_full_map(self, map):
        s = map
        s = self.add_hamsters_on_map(s)
        s = self.add_player_on_map(s)
        return s

    def add_hamsters_on_map(self, map):
        s = map
        for h in self.hamsters:
            if h.health > 0:
                s = self.add_point(h.position, str(h.id), s)
        return s

    def add_player_on_map(self, map):
        s = map
        s = self.add_point(self.player.position, 'x', s)
        return s

    def get_hamster_on_position(self, position):
        s = self.add_hamsters_on_map(self.map)
        return s.split('\n')[position[1]][position[0]]

    def on_move(self, dir):
        hamster = self.get_hamster_on_position(self.player.position)
        if not hamster == '*':
            self.player.on_shot(int(hamster))
            print('health:', self.player.health)
            if self.player.health <= 0:
                print('game over')
                self.gameon = False
                return False
            h = self.hamsters[int(hamster)-1]
            killed = h.on_shot()
            if killed:
                print(h.id, 'was killed')
            else:
                print(h.id, 'was shot')
                self.move_player(self.back[dir])

    def move_player(self, dir):
        if dir == 'w':
            if self.player.position[1] == 0:
                return False
            self.player.position[1] -= 1
        elif dir == 'a':
            if self.player.position[0] == 0:
                return False
            self.player.position[0] -= 1
        elif dir == 's':
            if self.player.position[1] == len(self.map.split('\n'))-1:
                return False
            self.player.position[1] += 1
        elif dir == 'd':
            if self.player.position[0] == len(self.map.split('\n')[0])-1:
                return False
            self.player.position[0] += 1
        else:
            return False
        self.on_move(dir)

    def wait(self):
        self.player.heal()
        print('health:', self.player.health)

    def start(self):
        self.gameon = True
        while self.gameon:
            if len([h for h in self.hamsters if h.health > 0]) == 0:
                print(self.happy_message)
                self.gameon = False

            cmd = input('Insert command: ')
            if cmd and cmd in 'wasd':
                self.move_player(cmd)
                self.render_map()
            if cmd == 'e':
                self.wait()
            if cmd == 'q':
                self.gameon = False


game = Game()

game.render_map()
game.start()

# 1. Исправлен баг выхода за пределы поля
# 2. Исправлено появление хомяка под игроком (процедура получения свободного поля учитывает положение игрока)
# 3. Исправлено определение выигрыша