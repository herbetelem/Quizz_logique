# coding : utf-8

# * import des libs
import pygame

class Model_button:
    
    def __init__(self, x, y):
        self.image = pygame.image.load('asset/button/block.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y