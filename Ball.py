import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((30,30))
        self.image.fill((255,0,0))

        self.rect = self.image.get_rect()
        self.rect.x = (800/2) - 15
        self.rect.y = (600/2) - 15

        self.x_velocity = 3
        self.y_velocity = 3

    def update(self):
        self.rect.x += self.x_velocity
        self.rect.y += self.y_velocity

        if(self.rect.y < 0):
            self.y_velocity *= -1
        if(self.rect.y > 600-30):
            self.y_velocity *= -1

    def collisionWithPaddles(self, paddleRight, paddleLeft):
        if(self.rect.x > paddleLeft.rect.x - 15):
            #if(self.rect.y > paddleLeft.rect.y and self.rect.y < paddleLeft.rect.y + 80):
            self.x_velocity *= -1
