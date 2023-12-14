import pygame

class Asset_Loader:
    def __init__(self):
        # MUSIC
        pygame.mixer.init()
        main_music = pygame.mixer.music.load("Driving home for christmas/assets/music/Driving Home For Christmas.mp3")
        

        # IMAGES
        self.player_image = pygame.image.load("Driving home for christmas/assets/images/GreenCar.png").convert_alpha()
        self.ground_image = pygame.image.load("Driving home for christmas/assets/images/snow-tilemap.png").convert_alpha()
        self.main_tree = pygame.image.load("Driving home for christmas/assets/images/main-tree.png").convert_alpha()