import os, pygame, json, random

BASE_IMG_PATH = "data/img/"

def load_image(path):
    img = pygame.image.load(BASE_IMG_PATH + path).convert()
    img.set_colorkey((0, 0, 0))
    return img
    
class DataManager:
    def __init__(self):
        self.zone_data = {}
        self.skill = self.load_json(f'data/skills.json')

    def load_zone(self, zone):
        self.zone_data = {
            'mobs': self.load_json(f'data/zones/{zone}/mobs.json'),
            'loot_tables': self.load_json(f'data/zones/{zone}/loot_tables.json'),
            'events': self.load_json(f'data/zones/{zone}/events.json'),
            'unique_mobs': self.load_json(f'data/zones/{zone}/unique_mobs.json')
        }
        
        self.current_zone = zone

    def load_json(self, path):
        with open(path, 'r') as f:
            return json.load(f)

    def load_mob(self, mob_id):
        return self.zone_data['mobs'].get(mob_id)

    def load_skill(self, skill_id):
        return self.zone_data['skills'].get(skill_id)

    def get_rand_mob(self, diff):
        pool = ()
        for en in self.zone_data['mobs']:
            if self.zone_data['mobs'][en]["difficulty_min"] <= diff:
                pool.append(en)

        if pool:
            return random.choice(pool)
        return None
