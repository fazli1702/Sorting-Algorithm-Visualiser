import pygame
from constant import *
from algorithm import *

pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WIN.fill(BLACK)
pygame.display.set_caption('Sorting Algorithm Visualiser')

sorts = [
    BubbleSort(WIN), 
    InsertionSort(WIN), 
    SelectionSort(WIN),
    MergeSort(WIN),
    QuickSort(WIN)
]

def main():
    run = True
    execute = False
    sort_algo = sorts[4]  # change index to change sorting algorithms

    while run:
        pygame.time.delay(10) # delay refresh

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    execute = True

        if execute:
            sort_algo.sort_lst()
            execute = False
        else:
            sort_algo.update()
        
    pygame.quit()



if __name__ == '__main__':
    main()