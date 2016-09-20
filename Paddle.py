import pygame

class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((15,80))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y 

        self.change_y = 0
        self.velocity = 9 # pixels per frame

    def update(self):
        self.rect.y += self.change_y * self.velocity

    def getInput(self, event, up_key, down_key):
        if(event.type == pygame.KEYDOWN):
            if(event.key == up_key):
                self.change_y = -1
            if(event.key == down_key):
                self.change_y = 1
        elif (event.type == pygame.KEYUP):
            if(event.key == up_key or event.key == down_key):
                self.change_y = 0
