import pygame
import os
from Ball.green_ball import Green_ball


class Game:
    def __init__(self):
        self.width = 1000
        self.height = 1000
        self.win = pygame.display.set_mode((self.width, self.width))
        self.cube = []
        self.ball = [Green_ball()]
        self.ball_qty = []
        self.score = []
        self.bg = pygame.image.load(os.path.join("game_assets", "bg.jpg"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.clicks = [] # remove


    def run(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                pos = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.clicks.append(pos)
                    print(self.clicks)

            # loop for Ball
            to_del = []
            for ba in self.ball:
                if ba.x < -5:
                    to_del.append(ba)

            # delete all balls off the screen

            for d in to_del:
                self.ball.remove(d)


            self.draw()

        pygame.quit()

    def draw(self):
        self.win.blit(self.bg, (0, 0))

        # draw ball

        for ba in self.ball:
            ba.draw(self.win)


        for p in self.clicks:
            pygame.draw.circle(self.win, (255, 0, 0), (p[0], p[1]), 5, 0)
        pygame.display.update()




g = Game()
g.run()