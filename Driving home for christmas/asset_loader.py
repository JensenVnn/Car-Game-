import pygame

class Asset_Loader:
    def __init__(self):
        # self.game = game
        
        # MUSIC
        pygame.mixer.init()
        main_music = pygame.mixer.music.load("Driving home for christmas/assets/music/Driving Home For Christmas.mp3")
        

        # IMAGES
        self.player_image = pygame.image.load("Driving home for christmas/assets/images/GreenCar.png").convert_alpha()