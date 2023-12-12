import pygame, sys

from settings import *
from sprites import *
from asset_loader import *

class Game:
    def __init__(self):
        self.running = True

        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_WIDTH))
        self.clock=pygame.time.Clock()

        self.asset_loader = Asset_Loader()

        pygame.mixer.music.play(-1)

    def draw(self):
        self.screen.fill("gray")

        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()

    def createTilemap(self):
        for i,row in enumerate(tilemap):
            for j,column in enumerate(row):
                if column=='B':
                    Block(self,j,i)
                if column == 'P':
                    Player(self,j,i)

    def main_menu(self):
        pass

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
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
        self.blocks = pygame.sprite.LayeredUpdates()

        self.createTilemap()

if __name__ == "__main__":
    game = Game()

    game.new()
    game.main()

    pygame.quit()
    sys.exit()