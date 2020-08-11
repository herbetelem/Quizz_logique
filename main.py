# coding : utf-8

# IMPORT
import pygame
import math
from game_file.game import Game
from game_file.score import Score
from game_file.variable_load import Variable_load
# INITIALISATION DE PYGAME
pygame.init()


# CREATION DE LA FENETRE
# LB Changer le titre de la fenêtre
pygame.display.set_caption("Quizz Logique")
# LB Dimensionner la fenêtre
screen = pygame.display.set_mode((1080, 720))


# CREATION DU MENU
# * HH importer et charger le background
background = pygame.image.load('asset/bg/bg_quizz.jpg')
background = pygame.transform.scale(background, (1080, 720))


# * HH import des boutons du menu
play_button = pygame.image.load('asset/button/new_game.png')
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 4) - 50
play_button_rect.y = math.ceil(screen.get_height() / 2)


score_button = pygame.image.load('asset/button/score.png')
score_button_rect = play_button.get_rect()
score_button_rect.x = math.ceil(screen.get_width() / 4) * 2 + 50
score_button_rect.y = math.ceil(screen.get_height() / 2)


# * HH Charge la Favicon
icon_32x32 = pygame.image.load("asset/Python.svg.png").convert_alpha()
# * HH Applique la Favicon
pygame.display.set_icon(icon_32x32)


# CREATION DES VAR NESCESSAIRE
game = Game(screen)
score = Score(screen)
variable_load = Variable_load(screen)
running = True


# LB tant que le running est égal True, la fenêtre s'affiche
while running :
    # * HH appliquer le background
    screen.blit(background, (0,0))
    if game.is_playing:
        game.update(screen) 

    elif score.score_look:
        score.update(screen)
        
    else:
        # * HH ajouter l'ecran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(score_button, score_button_rect)

    for event in pygame.event.get() :
        # LB Si l'event généré par l'utilisateur est de quitter
        if event.type == pygame.QUIT :
            running = False
            game.sql_request.connection.close()
            pygame.quit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # * HH verifier que lors du click de la souris, on est bien sur les boutons
            if play_button_rect.collidepoint(event.pos) and game.is_playing == False and score.score_look == False:
                game.is_playing = True
                game.player = False

            if score_button_rect.collidepoint(event.pos) and game.is_playing == False and score.score_look == False:
                score.score_look = True

            if score.home_rect.collidepoint(event.pos) and game.is_playing == False and score.score_look == True:
                score.score_look = False
    
            # * si une partie est lancé
            if game.is_playing and score.score_look == False:
                
                # Changer l'image du round si il est coché
                if variable_load.round1_rect.collidepoint(event.pos):
                    game.change_round(1)
                    game.choice_player = 1
                if variable_load.round2_rect.collidepoint(event.pos):
                    game.change_round(2)
                    game.choice_player = 2
                if variable_load.round3_rect.collidepoint(event.pos):
                    game.change_round(3)
                    game.choice_player = 3
                if variable_load.round4_rect.collidepoint(event.pos):
                    game.change_round(4)
                    game.choice_player = 4
                    
                # Changer la question réponse #* SI le joeur a selectionner un rond et l'a valider
                if variable_load.next_rect.collidepoint(event.pos)and game.round_check and game.player_validated:
                    if game.question == 5:
                        score.score = game.score
                        score.score_player()
                        game.question = 1
                        game.choice_player = 0
                        game.player = False
                        game.player_name = "Homer Simpson"
                        game.score = 0
                        score.score_look = True
                        game.is_playing = False
                        for round in range(4) :
                            game.list_round[round] = False
                        for bloc in game.list_bloc:
                            bloc.image = pygame.image.load('asset/button/block.png')
                    else:
                        game.next_question()
                    
                # * verifier la reponse du joueur
                if variable_load.validation_rect.collidepoint(event.pos) and game.round_check and game.player_validated == False:
                    game.check_answer()
                    
                # * check le click sur un champ
                for champ in game.list_champ:
                    if champ[0].rect.collidepoint(event.pos) and game.player == False:
                        game.player = True
                        game.player_name = champ[1]
                        score.player_name = champ[1]


    # * HH update le screen
    pygame.display.flip()
