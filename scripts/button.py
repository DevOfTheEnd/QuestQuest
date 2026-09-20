import pygame

class Button:
    def __init__(self, game, pos, size, content, size_increment):
        self.size = size
        self.pos = pos
        self.content = content
        self.game = game
        self.size_inc = size_increment
        self.inf = False

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
        
        
class MenuButton(Button):
    def clicked(self):
        mx, my = pygame.mouse.get_pos()
        mx //= 2
        my //= 2
        if self.button.collidepoint((mx, my)):
            return self.game.click