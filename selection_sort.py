import sys 
import random
import time


def SelSort(A):
    
    for i in range(len(A)): 
      
        min_idx = i 
        for j in range(i+1, len(A)): 
            if A[min_idx] > A[j]: 
                min_idx = j 
              
        
        A[i], A[min_idx] = A[min_idx], A[i]







L = []
for j in range(1000):
        L.append(random.randint(0,200))

start = time.time()
SelSort(L)
end = time.time()
print("\nSorted Field:")
print(L)
    
print("\nTime:")
print(end-start)



