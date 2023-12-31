import pygame

from settings import *
from asset_loader import *

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE * 2

        self.x_change = 0
        self.y_change = 0

        self.facing = "up"

        self.turbo = False

        self.image = self.game.asset_loader.player_image_up

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.movement()
        self.animations()

        self.rect.x += self.x_change
        self.collision("x")
        self.rect.y += self.y_change
        self.collision("y")

        self.x_change = 0
        self.y_change = 0

        if self.game.win:
            self.image = self.game.asset_loader.weezer_image
            self.image = pygame.transform.scale(self.image,[self.width * 2, self.height * 2])

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            for sprite in self.game.all_sprites:
                sprite.rect.x += PLAYER_SPEED
            self.x_change -= PLAYER_SPEED
            self.facing = "left"

        if keys[pygame.K_RIGHT]:
            for sprite in self.game.all_sprites:
                sprite.rect.x -= PLAYER_SPEED
            self.x_change += PLAYER_SPEED
            self.facing = "right"

        if keys[pygame.K_UP]:
            for sprite in self.game.all_sprites:
                sprite.rect.y += PLAYER_SPEED
            self.y_change -= PLAYER_SPEED
            self.facing = "up"

        if keys[pygame.K_DOWN]:
            for sprite in self.game.all_sprites:
                sprite.rect.y -= PLAYER_SPEED
            self.y_change += PLAYER_SPEED
            self.facing = "down"

        if keys[pygame.K_LCTRL]:
            if self.game.turbo_cooldown > 300:
                self.turbo = True
            else:
                self.turbo = False

    def animations(self):
        global PLAYER_SPEED

        up_animation = self.game.asset_loader.player_image_up
        down_animation = self.game.asset_loader.player_image_down
        left_animation = self.game.asset_loader.player_image_left
        right_animation = self.game.asset_loader.player_image_right
        turbo = self.game.asset_loader.player_image_turbo

        if self.facing == "down":
            self.image = down_animation

        if self.facing == "up":
            self.image = up_animation

        if self.facing == "left":
            self.image = left_animation

        if self.facing == "right":
            self.image = right_animation

        if self.turbo:
            self.image = turbo
            PLAYER_SPEED = 8
            if self.game.cooldown > 180:
                self.game.cooldown = 0
                PLAYER_SPEED = 3
                self.turbo = False


    def collision(self, direction):
        if direction == "x":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            hit_present = pygame.sprite.spritecollide(self, self.game.present_blocks, True)
            if hits:
                if self.x_change > 0:
                    for sprite in self.game.all_sprites:
                        sprite.rect.x += PLAYER_SPEED
                    self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_change < 0:
                    for sprite in self.game.all_sprites:
                        sprite.rect.x -= PLAYER_SPEED
                    self.rect.x = hits[0].rect.right
            if hit_present:
                self.game.present_count += 1
        
        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            hit_present = pygame.sprite.spritecollide(self, self.game.present_blocks, True)
            if hits:
                if self.y_change > 0:
                    for sprite in self.game.all_sprites:
                        sprite.rect.y += PLAYER_SPEED
                    self.rect.y = hits[0].rect.top - self.rect.height
                if self.y_change < 0:
                    for sprite in self.game.all_sprites:
                        sprite.rect.y -= PLAYER_SPEED
                    self.rect.y = hits[0].rect.bottom
            if hit_present:
                self.game.present_count += 1

class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.asset_loader.main_tree
        self.image = pygame.transform.scale(self.image, [self.width * 1.5, self.height * 1.75])

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Ground(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites, self.game.ground_blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.asset_loader.ground_image

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Present_Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites, self.game.present_blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE + 200
        self.height = TILESIZE + 200

        self.image = self.game.asset_loader.present_image

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    
    def update(self):
        if self.game.win:
            self.kill()