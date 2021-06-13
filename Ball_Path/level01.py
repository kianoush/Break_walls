import pygame
import math



class Ball_path:
    imgs = []
    def __init__(self):
        self.width = 64
        self.height = 64
        self.health = 1
        self.path = 0
        self.x = 500
        self.y = 1000
        self.img = None
        self.dis = 0
        self.animation_count = 0
        self.path_pos = [(500, 1000)]
        self.move_count = 0
        self.move_dis = 0


    def draw(self, win):
        """

        :param win:
        :return:
        """
        self.img = self.imgs[self.animation_count//3]
        self.animation_count += 1
        if self.animation_count >= len(self.imgs)*3:
            self.animation_count = 0

        win.blit(self.img, (self.x, self.y))
        self.move()


    def collide(self, X, Y):
        """

        :param x:
        :param y:
        :return:
        """
        print("Collide= ", X, Y)
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.health  and  Y >= self.y:
                print("Collide= ", X,Y)
                return True
        return False


    def move(self):
        """

        :return:
        """
        x1, y1 = [500, 1000]
        print(x1, y1)

        if x1 >= 1000 or x1 <= 0 or y1 >= 1000 or y1 <= 0:
            x2,y2 = x1 / 2, y1 / 2
        else:
            x2, y2 = x1 * 2, y1 * 2

        self.x = x2
        self.y = y2
        return True


        # if self.path_pos + 1 >= len(self.path):
        #     x2, y2 = (795, 453)
        # else:

        #     x2, y2 = self.path[self.path_pos+1]
        #
        # move_dis = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        #
        # self.move_count += 1
        # drin = (x2-x1, y2-y1)
        #
        # move_x, move_y = (self.x + drin[0] * self.move_count, self.y + drin[1] * self.move_count)
        # self.dis += math.sqrt((move_x - x1) ** 2 + (move_y - y1) ** 2)
        #
        # # Go to next point
        # if self.dis >= move_dis:
        #     self.dis = 0
        #     self.move_count = 0
        #     self.path_pos += 1
        #     if self.path_pos >= len(self.path):
        #         return False

        #
        # self.x = move_x
        # self.y = move_y
        return True

    def hit(self):
        self.health -= 1
        if self.health <= 0:
            return True