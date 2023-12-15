import pygame

from settings import *

class Asset_Loader:
    def __init__(self, game):
        self.game = game
        # MUSIC
        pygame.mixer.init()
        main_music = pygame.mixer.music.load("Driving home for christmas/assets/music/Driving Home For Christmas.mp3")
        

        # IMAGES
        self.main_tree = pygame.image.load("Driving home for christmas/assets/images/main-tree.png").convert_alpha()

        self.player_image_up = pygame.image.load("Driving home for christmas/assets/images/GreenCar_up.png").convert_alpha()
        self.player_image_down = pygame.image.load("Driving home for christmas/assets/images/GreenCar_down.png").convert_alpha()
        self.player_image_left = pygame.image.load("Driving home for christmas/assets/images/GreenCar_left.png").convert_alpha()
        self.player_image_right = pygame.image.load("Driving home for christmas/assets/images/GreenCar_right.png").convert_alpha()
        self.player_image_turbo = pygame.image.load("Driving home for christmas/assets/images/GreenCar-Turbo.png").convert_alpha()

        self.ground_image = pygame.image.load("Driving home for christmas/assets/images/snow-tilemap.png").convert_alpha()

        self.present_image = pygame.image.load("Driving home for christmas/assets/images/WhitePresent.png")
        self.weezer_image = pygame.image.load("Driving home for christmas/assets/images/weezer.jpg")
    