import pygame, sys 
from level import Level
from settings import *

'''
This file is for running the game
'''
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Investment Valley") # set show game title
        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            dt = self.clock.tick() / 1000
            self.level.run(dt)
            pygame.display.update()
        
        
if __name__ == '__main__':
    game = Game()
    game.run() # run the game