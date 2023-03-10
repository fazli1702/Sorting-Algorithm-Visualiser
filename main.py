import pygame
from constant import *
from algorithm import *
from sys import argv

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

    while run:
        pygame.time.delay(10) # delay refresh

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    execute = True

        if execute:
            SORT_ALGO.sort_lst()
            execute = False
        else:
            SORT_ALGO.update()
        
    pygame.quit()



if __name__ == '__main__':
    SORT_ALGO = None

    if len(argv) > 1:
        for ele in argv[1:]:
            ele = ele[1:].lower()  # remove "-"

            if ele.isalpha():  # sort algorithm
                if ele == 'b':
                    SORT_ALGO = sorts[0]
                if ele == 'i':
                    SORT_ALGO = sorts[1]
                if ele == 's':
                    SORT_ALGO = sorts[2]
                if ele == 'm':
                    SORT_ALGO = sorts[3]
                if ele == 'q':
                    SORT_ALGO = sorts[4]
                if ele == 'h':  # help
                    print('''
                    main.py -b -n

                        sorting algorithm
                        -b  bubble sort
                        -i  insertion sort
                        -s  selection sort
                        -m  merge sort
                        -q  quick sort

                        time delay
                        -n  default n = 100

                        Press [SPACE] to start visualisation
                        Press [ENTER] to close visualisation

                    ''')


            if ele.isdigit():  # time delay
                if not SORT_ALGO:
                    SORT_ALGO = sorts[0]
                SORT_ALGO.set_delay(int(ele))
                    
    else:
        SORT_ALGO = sorts[0]

    main()