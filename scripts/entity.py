
class Entity:
    def __init__(self, hp, skill, type):
        self.type = type
        self.skill = skill
        self.hp_max = hp
        self.hp = hp
        self.effects = {}

    def update(self):
        if self.hp > self.hp_max:
            self.hp = self.hp_max

class PlayerEntity:
    def __init__(self, class_id):
        self.stats = {
            'INT': 0,
            'STR': 0,
            'DEX': 0,
            'CHA': 0,
            'CON': 0,
            'MAR': 0,
            'TAC': 0,
        }

        self.base_skill = ['strike', 'guard']
        self.effects = {}

    def actualise_stats(self):
        self.dmg_red = 0 + 0.1 * self.stats['CON']


        
