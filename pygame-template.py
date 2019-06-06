import pygame
import sys
from pygame.locals import *
import os
os.environ['SDL_VIDEO_CENTERED'] = '1'


class Game(object):

    def __init__(self, CAPTION="My game", WIDTH=800, HEIGHT=600):
        pygame.init()
        self.isRunning = True
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.CAPTION = CAPTION
        self.FPS = 30
        self.clock = pygame.time.Clock()
        display = pygame.display
        self.screen = display.set_mode(
            (self.WIDTH, self.HEIGHT),   pygame.HWSURFACE)

        display.set_caption(self.CAPTION)

    def __destroy_game(self):
        self.isRunning = False
        pygame.quit()
        sys.exit(0)

    def run(self):
        while self.isRunning:
            self.clock.tick(self.FPS)

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.__destroy_game()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.__destroy_game()
                    elif event.key == K_LEFT:
                        print("LEFT DOWN")
                    elif event.key == K_RIGHT:
                        print("RIGHT DOWN")

            self.screen.fill((255, 255, 0))
            pygame.display.update()


if __name__ == '__main__':
    g = Game()
    g.run()
