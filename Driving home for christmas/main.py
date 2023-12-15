import pygame, sys, random

from settings import *
from sprites import *

class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()

        self.font = pygame.font.Font(None, 100)

        self.running = True
        self.win = False

        self.cooldown = 0

        self.present_count = 0

        self.turbo_cooldown = 300

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

        self.asset_loader = Asset_Loader(self)

        pygame.mixer.music.play(-1)

    def createTilemap(self):
        for i,row in enumerate(tilemap):
            for j,column in enumerate(row):
                Ground(self, j, i)
                if column=='B':
                    Block(self,j,i)
                if column == 'P':
                    Player(self,j,i)
                if column == '.':
                    if random.randint(1, 15) == 1:
                        Present_Block(self,j,i)
                    else:
                        pass

    def draw(self):
        self.screen.fill((242, 237, 241))

        if self.present_count < 10:
            self.score_text = self.font.render(f"Score: {self.present_count}", True, ("red"))
        else:
            self.win = True
            self.score_text = self.font.render("You won!", True, ("green"))

        pos = pygame.mouse.get_pos() 
        # giving color and shape to the circle 

        self.clock.tick(FPS)
        self.all_sprites.draw(self.screen)
        self.screen.blit(self.score_text, (WIN_WIDTH // 2, 10))
        pygame.display.update()

    def update(self):
        self.cooldown += 1

        self.all_sprites.update()

    def new(self):
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.ground_blocks = pygame.sprite.LayeredUpdates()
        self.present_blocks = pygame.sprite.LayeredUpdates()

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