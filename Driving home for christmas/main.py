import pygame, sys

from settings import *
from asset_loader import *
from sprites import *

class Game:
    def __init__(self):
        pygame.init()

        self.running = True

        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

        self.asset_loader = Asset_Loader()

        pygame.mixer.music.play(-1)

    def createTilemap(self):
        for i,row in enumerate(tilemap):
            for j,column in enumerate(row):
                Ground(self, j, i)
                if column=='B':
                    Block(self,j,i)
                if column == 'P':
                    Player(self,j,i)

    def draw(self):
        self.screen.fill("gray")

        self.clock.tick(FPS)
        self.all_sprites.draw(self.screen)
        pygame.display.update()

    def update(self):
        self.all_sprites.update()

    def new(self):
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.ground_blocks = pygame.sprite.LayeredUpdates()

        self.createTilemap()


    def main(self):
        while self.running:
            self.events()
            self.draw()
            self.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

if __name__ == "__main__":
    game = Game()

    game.new()
    game.main()

    pygame.quit()
    sys.exit()