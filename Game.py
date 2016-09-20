import pygame

# Importing all the classes needed for the game
from Paddle import Paddle
from Ball import Ball

class Game:
    def __init__(self):
        pygame.init()

        # Screen dimensions used for various calculations
        self.width = 800
        self.height = 600

        self.isRunning = True # initial value should be True at start
        
        self.screen = pygame.display.set_mode((self.width,self.height)) # The game screen
        self.clock = pygame.time.Clock() # Clock for limiting frames per second
        
        self.all_sprites_list = pygame.sprite.Group() # sprite list contating all the game sprites
        self.player_one = Paddle(20, 5) # Creating an object called player_one
        self.player_two = Paddle(self.width-20 - 15, 5)
        self.all_sprites_list.add(self.player_one, self.player_two) # Adding player_one to our sprite list

        self.ball = Ball()
        self.all_sprites_list.add(self.ball)
        
    def run(self):
        while self.isRunning:
            for event in pygame.event.get():
                self.player_one.getInput(event, pygame.K_w, pygame.K_s)
                self.player_two.getInput(event, pygame.K_UP, pygame.K_DOWN)
                if event.type == pygame.QUIT: # If the user clicked QUIT then exit out
                    self.isRunning = False

            self.screen.fill((0,0,0)) # Filling the screen with the color black

            # Update and draw all sprites
            self.all_sprites_list.update()
            self.all_sprites_list.draw(self.screen)
            self.ball.collisionWithPaddles(self.player_one, self.player_two)

            self.clock.tick(60)            
            pygame.display.update()
            
        pygame.quit()
