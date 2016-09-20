import pygame

class Game:
    def __init__(self):
        pygame.init()
            
        self.width = 800
        self.height = 600

        self.isRunning = True
        
        self.screen = pygame.display.set_mode((self.width,self.height))
        self.clock = pygame.time.Clock()
        
    def run(self):
        while self.isRunning:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isRunning = False

            self.screen.fill((255,255,255))


            self.clock.tick(60)            
            pygame.display.update()
            
        pygame.quit()
