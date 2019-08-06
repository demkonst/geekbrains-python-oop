from random import randint


class Player:
    max_health = 20
    health = 20
    default_damage = 10
    position = [0, 0]

    def on_shot(self, dmg):
        self.health -= randint(0, dmg)
        return self.health == 0

    def heal(self):
        if self.health < self.max_health:
            self.health += 1
