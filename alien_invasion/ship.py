import pygame

class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        """IDE USE r to read the ship.bmp from a absolute path"""
        self.image = pygame.image.load(r'D:\code\explore_the_word\alien_invasion\images\ship.bmp') 
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        