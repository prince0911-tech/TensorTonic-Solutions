import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    A=np.array(A)
    m,n=np.shape(A)
    b=np.zeros((n,m))

    for i in range(m):
        for j in range(n):
            b[j,i]=A[i,j]
    return b
    pass
