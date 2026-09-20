import pygame, sys
import time
from scripts.utils import load_image, DataManager
from scripts.button import Button, MenuButton
from scripts.select_screen import ClassSelect, SelectClassButton
from scripts.entity import Entity, PlayerEntity

class Game:

    def __init__(self):

        pygame.init()

        pygame.display.set_caption("Quest Quest")
        self.screen = pygame.display.set_mode((1280, 960))
        self.display = pygame.Surface((self.screen.get_width()/2, self.screen.get_height()/2))
        self.clock = pygame.time.Clock()
        self.is_menu = True
        self.select_menu = False
        self.in_game = False

        self.assets = {
            'menu_background': load_image('menu_background.png'),
            'start_button': load_image('UI/start.png'),
            'quit_button': load_image('UI/quit.png'),
            'select_background': load_image('select_background.png'),
            'placeholder': load_image('placeholder')
        }
        self.data_manager = DataManager()
        self.current_zone = None

        self.active_buttons = []

        self.class_id = ""
        self.last_click_time = 0
        self.click_cooldown = 0.2

        self.setup_menu()

    def clear_buttons(self):
        self.active_buttons = []

    def add_button(self, button):
        self.active_buttons.append(button)

    def setup_menu(self):
        #Menu buttons
        self.clear_buttons()
        self.start_button = MenuButton(self, (160, 216), (320, 48), self.assets['start_button'], 8)
        self.quit_button = MenuButton(self, (160, 312), (320, 48), self.assets['quit_button'], 8)
        self.add_button(self.start_button)
        self.add_button(self.quit_button)

    def setup_select(self):
        self.class_id = ""
        self.clear_buttons()
        self.select = ClassSelect(self)
        for button in self.select.buttons:
            self.add_button(button)

    def enter_zone(self, zone_name):
        self.data_manager.load_zone(zone_name)
        self.current_zone = zone_name

    def prepare_run(self):
        self.player = PlayerEntity(self.class_id)

    def try_img(self, asset):
        if asset in self.assets:
            return self.assets[asset]
        else:
            try:
                return load_image(asset)
            except:
                return self.assets['placeholder']

    def run(self):
        while True:
            if self.is_menu:
                self.display.blit(self.assets['menu_background'], (0, 0))
            elif self.select_menu:
                self.display.blit(self.assets['select_background'], (0, 0))

            for button in self.active_buttons:
                button.update()
                if type(button) == SelectClassButton:
                    if button.clicked() and (time.time() - self.last_click_time) > self.click_cooldown:
                        self.class_id = button.class_id
                        self.last_click_time = time.time()
                        print(f"Selected: {button.class_id}")

            self.click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.click = True
                    
            if self.is_menu:
                if self.quit_button.clicked():
                    pygame.quit()
                    sys.exit()

                if self.start_button.clicked():
                    self.is_menu = False
                    self.select_menu = True
                    self.setup_select()

            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)
            

    
class Battle:
    def __init__(self, game, mob_id):
        self.game = game
        self.mob
        if type(mob_id) == "string":
            self.mob.append(game.data_manager.load_mob(mob_id))
        else:
            for mob in mob_id:
                self.mob.append(game.data_manager.load_mob(mob))

    def use_skill(self, user, skill):
        used_skill = self.game.data_manager.load_skill(skill)
        if used_skill['type'] == "attack":
            pass
        
        if used_skill['type'] == "buff":
            user.effects.append(used_skill['effect'])


Game().run()
