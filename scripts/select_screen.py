import pygame
import time
from scripts.button import Button

class ClassSelect:
    def __init__(self, game):
        self.game = game

        self.classes = ("Mage", "Clerc", "Warrior", "Ranger")

        self.positions = (
            (40, 20),
            (340, 20),
            (40, 220),
            (340, 220)
        )

        self.buttons = []

        for class_id, (class_name, pos) in enumerate(
            zip(self.classes, self.positions)
        ):
            self.buttons.append(
                SelectClassButton(
                    self.game,
                    pos,
                    (260, 160),
                    (0, 0, 0),
                    10,
                    self.classes[class_id]
                )
            )
                

class SelectClassButton(Button):

    def __init__(self, game, pos, size, content, size_increment, class_id):
        super().__init__(game, pos, size, content, size_increment)
        self.class_id = class_id


    def update(self):
        mx, my = pygame.mouse.get_pos()
        mx //= 2
        my //= 2
        self.button = pygame.Rect(self.pos, self.size)
        if self.button.collidepoint(mx, my):
            self.button.inflate_ip(self.size_inc, self.size_inc)
            self.inf = True
        else:
            self.inf = False

        if type(self.content) == tuple:
            pygame.draw.rect(self.game.display, self.content, self.button)
        else:
            self.game.display.blit(pygame.transform.scale(self.content, 
            (self.size[0] + self.size_inc*self.inf, self.size[1] + self.size_inc*self.inf)), 
            (self.pos[0] - (self.size_inc*self.inf)/2, self.pos[1] - (self.size_inc*self.inf)/2))

    def clicked(self):
        mx, my = pygame.mouse.get_pos()
        mx //= 2
        my //= 2
        if self.button.collidepoint((mx, my)):
            return self.game.click
        return False
