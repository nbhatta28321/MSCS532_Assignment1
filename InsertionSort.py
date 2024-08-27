
A = ([23,4,11,55,2,9,777], 7)
for i in range(0, 7):
    current = A[i]
    j=i

    while j > 0 and current > A[j-1]:
        temp = A[j-1]
        A[j-1] = A[j]
        A[j] = temp
        j=j-1                        

print(A)

