# coding : utf-8

# * import des libs
import pygame
from game_file.sql_function import SQL_request
from game_file.game import Game

# créer la classe game
class Score:
    
    def __init__(self, screen):
        # * definir si le jeu a commencer ou pas
        self.score_look = False
        # Vérifier si le joueur et déja dans le tableau des scores
        self.validation_user = ""
        # * definir l'objet sql
        self.sql_request = SQL_request()
        self.game = Game(screen)
        
        # ! Laura m'a fait enlever 10 lignes !
        # * definir l'objet retour au menu
        self.home = pygame.image.load('asset/home.png')
        self.home = pygame.transform.scale(self.home, (200, 75))
        self.home_rect = self.home.get_rect()
        self.home_rect.x = 65
        self.home_rect.y = 580
        
        # * def de nos score et nom
        self.player_name = ""
        self.score = 0


    def update(self, screen):
        # * je fait les update de mes different items
        self.sql_request.read_score()
        font = pygame.font.Font(None, 36)
        nb_vainqueur = len(self.sql_request.score_tmp)
        y_temp = 25
        for i in range(nb_vainqueur):
            phrase = f"{self.sql_request.score_tmp[i][1]} a obtenu le score de {self.sql_request.score_tmp[i][2]}"
            text = font.render(phrase, 1, (255,255,255))
            block = pygame.image.load('asset/button/block.png')
            block = pygame.transform.scale(block, (500, 50))
            screen.blit(block,(450, y_temp - 15))
            screen.blit(text,(500, y_temp))
            y_temp += 70
        # screen.blit(self.home, self.home_rect)

    # Envoyer les scores a la base de donnée 
    def score_player(self):
        self.sql_request.verification_user((self.player_name,))
        self.validation_user = self.sql_request.user
        # Si le jouer est deja dans la base de données
        if self.validation_user == True :
            self.sql_request.update_user(self.player_name, self.score)

        # Si le joueur n'est pas dans dans la base de données
        else :
            self.sql_request.create_score(self.player_name, self.score) 
            