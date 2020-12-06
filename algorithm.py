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
        self.delay = 300
        self.end_delay = 3000

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
        pygame.time.delay(self.delay)

    def end(self):
        self.set_all_colour(GREEN)
        self.update()
        print('Press [enter] to quit')

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        sys.exit(0)
        



class BubbleSort(Sort):
    def __init__(self, win):
        super().__init__(win)

    def sort_lst(self):
        self.bubble_sort()
        self.end()

    def bubble_sort(self):
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

            sorted_node = self.get_node(end)
            sorted_node.set_is_sorted(True)
            end -= 1


class InsertionSort(Sort):
    def __init__(self, win):
        super().__init__(win)

    def sort_lst(self):
        self.insertion_sort()
        self.end()

    def insertion_sort(self):
        start_node = self.get_node(0)
        start_node.set_is_sorted(True)

        for i in range(1, len(self.lst)):
            curr_node = self.get_node(i)
            curr_node.set_colour(RED)
            j = i - 1
            while j >= 0:
                self.set_standard_colour()
                prev_node, new_curr_node = self.get_node(j), self.get_node(j+1)
                prev_node.set_colour(RED)
                new_curr_node.set_colour(YELLOW)
                new_curr_node.set_is_sorted(True)
                if not curr_node.get_value() < prev_node.get_value():
                    break

                self.swap(j, j + 1)
                self.update()
                
                j -= 1


class SelectionSort(Sort):
    def __init__(self, win):
        super().__init__(win)

    def sort_lst(self):
        self.selection_sort()
        self.end()

    def insertion_sort(self):
        for i in range(len(self.lst)):
            curr_node = self.get_node(i)
            min_node, min_i = curr_node, i

            for j in range(i+1, len(self.lst)):
                next_node = self.get_node(j)
                self.set_standard_colour()
                curr_node.set_colour(RED)
                next_node.set_colour(RED)
                if min_i != i:
                    min_node.set_colour(YELLOW)

                if min_node.get_value() > next_node.get_value():
                    min_node, min_i = next_node, j

                self.update()
                
            self.swap(i, min_i)
            min_node.set_is_sorted(True)
            self.update()
            pygame.time.delay(self.delay)


class MergeSort(Sort):
    def __init__(self, win):
        super().__init__(win)

    def sort_lst(self):
        self.merge_sort(self.lst)
        self.end()

    def merge_sort(self, lst):
        pass
        


class QuickSort(Sort):
    def __init__(self, win):
        super().__init__(win)

    def sort_lst(self):
        self.quick_sort(0, len(self.lst) - 1)
        self.end()

    def quick_sort(self, low, high):
        if low < high:
            mid = self.partition(low, high)
            self.quick_sort(low, mid - 1)
            self.quick_sort(mid + 1, high)

    def partition(self, low, high):
        pivot_node = self.lst[low]
        left_ptr = low + 1
        right_ptr = high
        done = False

        while not done:
            left_node, right_node = self.get_node(left_ptr), self.get_node(right_ptr)

            while left_node.get_value() <= pivot_node.get_value():
                self.set_standard_colour()
                left_node.set_colour(RED)
                pivot_node.set_colour(YELLOW)
                self.update()

                left_ptr += 1
                if left_ptr > right_ptr:
                    break
                left_node = self.get_node(left_ptr)

            while right_node.get_value() >= pivot_node.get_value():
                self.set_standard_colour()
                right_node.set_colour(BLUE)
                pivot_node.set_colour(YELLOW)
                self.update()

                right_ptr -= 1
                if left_ptr > right_ptr:
                    break
                right_node = self.get_node(right_ptr)

            if left_ptr > right_ptr:
                done = True

            else:
                self.swap(left_ptr, right_ptr)

        self.swap(low, right_ptr)

        return right_ptr
        


    