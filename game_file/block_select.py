# coding : utf-8

# * import des libs
import pygame

class Block_select:
    
    def __init__(self, x, y):
        self.size = (205, 113)
        self.image = pygame.Surface(self.size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y