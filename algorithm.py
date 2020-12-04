import pygame
import sys
from constant import *
from random import randint


class Node:
    def __init__(self, value):
        self.value = value
        self.colour = WHITE
        self.is_sorted = False

    def __repr__(self):
        return str(self.value)

    def get_value(self):
        return self.value

    def get_height(self):
        return self.value * RECT_HEIGHT

    def get_colour(self):
        return self.colour

    def get_is_sorted(self):
        return self.is_sorted

    def set_colour(self, c):
        self.colour = c

    def set_is_sorted(self, n):
        self.is_sorted = n

    def get_coordinate(self, i):
        x = i * RECT_WIDTH
        y = HEIGHT - self.get_height()
        return x, y

    def display(self, win, i):
        x, y = self.get_coordinate(i)
        const = 5
        rect = ((x + const, y), (RECT_WIDTH - const, self.get_height()))
        pygame.draw.rect(win, self.colour, rect)

        # render text - show value
        pygame.font.init()
        font_size = 20
        font = pygame.font.SysFont('Consolas', font_size)
        text = font.render(str(self.value), True, BLACK)
        win.blit(text, (x + RECT_WIDTH // 2 - font_size // 2, HEIGHT - font_size))


class Sort:
    def __init__(self, win):
        self.lst = []
        self.win = win

        for i in range(WIDTH // RECT_WIDTH):
            while True:  # don't include any duplicate
                value = randint(1, 25)
                if value not in self.lst:
                    self.lst.append(value)
                    break
        self.lst = [Node(i) for i in self.lst]
    
    def get_node(self, i):
        return self.lst[i]

    def swap(self, i, j):
        self.lst[i], self.lst[j] = self.lst[j], self.lst[i]

    def set_standard_colour(self):
        for node in self.lst:
            if node.get_is_sorted():
                node.set_colour(GREEN)
            else:
                node.set_colour(WHITE)

    def set_all_colour(self, colour):
        for node in self.lst:
            node.set_colour(colour)

    def update(self):
        self.win.fill(BLACK)
        for i, node in enumerate(self.lst):
            node.display(self.win, i)
        pygame.display.update()



class BubbleSort(Sort):
    def __init__(self, win):
        super().__init__(win)

    def sort_lst(self):
        end = len(self.lst) - 1
        while end != 0:
            for i in range(end):
                self.set_standard_colour()
                curr_node, next_node = self.get_node(i), self.get_node(i+1)
                curr_node.set_colour(RED)
                next_node.set_colour(RED)

                if curr_node.get_value() > next_node.get_value():
                    self.swap(i, i+1)

                self.update()
                pygame.time.delay(100)

            sorted_node = self.get_node(end)
            sorted_node.set_is_sorted(True)
            end -= 1

        self.set_all_colour(GREEN)
        self.update()
        pygame.time.delay(3000)
        sys.exit(0)





    