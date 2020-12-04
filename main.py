import pygame
from constant import *
from algorithm import * 

pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WIN.fill(BLACK)
pygame.display.set_caption('Sorting Algorithm Visualiser')

FPS = 1

def main():
    run = True
    sorting = BubbleSort(WIN)
    execute= False

    while run:
        pygame.time.delay(10) # delay refresh

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    execute = True

        if execute:
            sorting.sort_lst()
        else:
            sorting.update()

        

    pygame.quit()

if __name__ == '__main__':
    main()