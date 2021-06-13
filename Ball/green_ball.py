import pygame
import os
from Ball_Path.level01 import Ball_path

class Green_ball(Ball_path):

    imgs = []

    for x in range(8):
        add_str = str(x)
        if x < 8:
            add_str = "0" + add_str
        imgs.append(pygame.transform.scale(
            pygame.image.load(os.path.join("game_assets/enemies/1", "1_enemies_1_RUN_0" + add_str + ".png")),
            (70, 70)))

