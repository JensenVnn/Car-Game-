import pygame, sys

from settings import *
from sprites import *

class Game:
    def __init__(self):
        self.running = True

        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_WIDTH))
        pygame.display.set_caption("blue square that moves across the screen")
        icon = pygame.image.load('Driving home for christmas/assets/images/0000FF.png.png').convert_alpha()
        pygame.display.set_icon(icon)
        self.clock=pygame.time.Clock()


        pygame.mixer.init()
        pygame.mixer.music.load("Driving home for christmas/assets/music/Driving Home For Christmas.mp3")
        pygame.mixer.music.play(-1)

    def draw(self):
        self.screen.fill("gray")

        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.all_sprites.update()

    def main(self):
        while self.running:
            self.events()
            self.draw()
            self.update()
            
    def new(self):
        self.all_sprites = pygame.sprite.LayeredUpdates()

        self.player = Player(self, 1, 1)

if __name__ == "__main__":
    game = Game()

    game.new()
    game.main()

    pygame.quit()
    sys.exit()