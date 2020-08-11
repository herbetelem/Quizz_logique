# coding : utf-8

# IMPORT
import pygame
import math


# Créer la class import variable
class Variable_load:

    def __init__(self, screen):

        # print logo LoL
        self.lol = pygame.image.load('asset/button/LoL.png')
        self.lol_rect = self.lol.get_rect()
        self.lol_rect.x = 10
        self.lol_rect.y = 10

        # print le cadre du titre 
        self.title = pygame.image.load('asset/button/title.png')
        self.title = pygame.transform.scale(self.title, (700, 125))
        self.title_rect = self.title.get_rect()
        self.title_rect.x = self.lol.get_width() + 50
        self.title_rect.y = math.ceil(screen.get_height() / 40)


        # Print block basique sans validation
        self.block = pygame.image.load('asset/button/block.png')
        self.block_rect = self.block.get_rect()
        self.block_rect.x = self.lol.get_width() + 50
        self.block_rect.y = math.ceil(screen.get_height() / 35 + 250)


        # Print block pour la bonne réponse
        self.block_right = pygame.image.load('asset/button/block_right.png')
        self.block_right_rect = self.block_right.get_rect()
        self.block_right_rect.x = self.lol.get_width() + 50
        self.block_right_rect.y = 0

        # Print block pour mauvaise réponse
        self.block_wrong = pygame.image.load('asset/button/block_wrong.png')
        self.block_wrong_rect = self.block_wrong.get_rect()
        self.block_wrong_rect.x = 0
        self.block_wrong_rect.y = 0

        # Print rond1 a cocher
        self.round1 = pygame.image.load('asset/button/round.png')
        self.round1_rect = self.round1.get_rect()
        self.round1_rect.x = self.lol.get_width()
        self.round1_rect.y = math.ceil(screen.get_height() / 35 + 225)

        # Print rond2 a cocher
        self.round2 = pygame.image.load('asset/button/round.png')
        self.round2_rect = self.round2.get_rect()
        self.round2_rect.x = self.lol.get_width()
        self.round2_rect.y = self.round1_rect.y + 110

        # Print rond3 a cocher
        self.round3 = pygame.image.load('asset/button/round.png')
        self.round3_rect = self.round3.get_rect()
        self.round3_rect.x = self.lol.get_width()
        self.round3_rect.y = self.round2_rect.y + 110

        # Print rond4 a cocher
        self.round4 = pygame.image.load('asset/button/round.png')
        self.round4_rect = self.round4.get_rect()
        self.round4_rect.x = self.lol.get_width()
        self.round4_rect.y = self.round3_rect.y + 110

        # Print rond coché
        self.round_selected = pygame.image.load('asset/button/round_selected.png')
        self.round_selected_rect = self.round_selected.get_rect()
        self.round_selected_rect.x = 0
        self.round_selected_rect.y = 0

        # Print rectangle pour passer a la question suivante 
        self.next = pygame.image.load('asset/button/next.png')
        self.next_rect = self.next.get_rect()
        self.next_rect.x = screen.get_width() - 290
        self.next_rect.y = screen.get_height() - 150

        # Print la case validation de la réponse
        self.validation = pygame.image.load('asset/button/validation.png')
        self.validation_rect = self.validation.get_rect()
        self.validation_rect.x = screen.get_width() - 290
        self.validation_rect.y = screen.get_height() - 150