# Sorting Algorithm Visualiser

This program visualise the different type of sorting algorithm (more to be added)
- Bubble sort 
- Insertion sort
- Selection sort
- Merge sort
- Quick sort

## Setup
Install required pacakages
```
$ pip install pygame
```

Run main.py
```
$ python main.py
```

Enter space bar to start the visulisation  
Close the window or press enter to close the window

## Customization
### Changing sorting algorithm
main.py, line 11 - 17
```
sorts = [
    BubbleSort(WIN), 
    InsertionSort(WIN), 
    SelectionSort(WIN),
    MergeSort(WIN),
    QuickSort(WIN)
]
```

In order to change the sorting algorithm, change the following line
main.py, line 22
```
sort_algo = sorts[n] # where n is 0 - 5
```

### Time delay
To increase the speed of the sort, change the following line  
algorithm.py, line 56
```
self.delay = n
```
The smaller the value of n, the faster the visualisation will execute
