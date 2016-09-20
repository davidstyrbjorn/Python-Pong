import pygame

class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.__init__(self)

        self.image = pygame.Surface((15,25))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.change_x = 0
        self.change_y = =

    def getInput(self, event, up_key, down_key, right_key, left_key):

    def move(self):
        

    def update(self):
        
