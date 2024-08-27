def insertion_sort_decresing_order(A, n):

    for i in range(0, n): # loop through each index in the Array list
        current = A[i] # created a variable to point to the current value for sorting
        j=i #assign the first value to variable

    # run the loop until previous value is grater than current for descending order.
        while j > 0 and current > A[j-1]: 
            #swap the value and point the index of j to current value
            temp = A[j-1] 
            A[j-1] = A[j]
            A[j] = temp
            j=j-1                        
  
    print(A)


# function to do the insertion sort and print the value
insertion_sort_decresing_order([23,4,11,55,2,9,777], 7)
