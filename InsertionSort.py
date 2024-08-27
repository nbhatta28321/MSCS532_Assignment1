def insertion_sort_decresing_order(A, n):

    for i in range(0, n):
        current = A[i]
        j=i

        while j > 0 and current > A[j-1]:
            temp = A[j-1]
            A[j-1] = A[j]
            A[j] = temp
            j=j-1                        
  
    print(A)

insertion_sort_decresing_order([23,4,11,55,2,9,777], 7)
