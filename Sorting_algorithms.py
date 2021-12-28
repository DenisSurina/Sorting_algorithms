import sys 
import random
import time


#selection sort
def SelSort(listA):
    
    for i in range(len(listA)): 
      
        min_idx = i 
        for j in range(i+1, len(listA)): 
            if listA[min_idx] > listA[j]: 
                min_idx = j 
              
        
        listA[i], listA[min_idx] = listA[min_idx], listA[i]


#Bubble sort

def BubbleSort(listA):

    n = len(listA)
    
    for i in range(n):

        swapped = False

        for j in range(0,n-i-1):
            if listA[j] > listA[j+1] : 
                listA[j], listA[j+1] = listA[j+1], listA[j] 
                swapped = True

        if swapped == False:
            break


#insertion sort

def InsertionSort(listA):

    for i in range(1,len(listA)):
        key = listA[i]

        j = i-1
        while j >=0 and key < listA[j] : 
                listA[j+1] = listA[j] 
                j -= 1
        listA[j+1] = key 
    

#shell sort

def ShellSort(arr): 
  
    n = len(arr) 
    gap = n//2
 
    while gap > 0: 
        
        for i in range(gap,n): 
  
            temp = arr[i] 
 
            j = i 
            while  j >= gap and arr[j-gap] >temp: 
                arr[j] = arr[j-gap] 
                j -= gap 
  
            arr[j] = temp 

        gap //= 2


#display of selection sort
A = []
for j in range(100):
        A.append(random.randint(0,200))

start = time.time()
SelSort(A)
end = time.time()
print("\nSorted field using selection sort:")
print(A)
print("\nTime:")
print(end-start)


#display of bubble sort
B = []
for j in range(100):
        B.append(random.randint(0,200))

start = time.time()
BubbleSort(B)
end = time.time()
print("\nSorted field using bubble sort:")
print(B)
print("\nTime:")
print(end-start)



#display of insertion sort
C = []
for j in range(100):
        C.append(random.randint(0,200))

start = time.time()
InsertionSort(C)
end = time.time()
print("\nSorted field using insertion sort:")
print(C)
print("\nTime:")
print(end-start)



#display of shell sort
D = []
for j in range(100):
        D.append(random.randint(0,200))

start = time.time()
ShellSort(D)
end = time.time()
print("\nSorted field using shell sort:")
print(D)
print("\nTime:")
print(end-start)



