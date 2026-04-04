import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here
    A=np.array(A)
    m,n=np.shape(A)
    trace=0
    for i in range(m):
        for j in range(n):
            if i==j:
                trace=trace+A[i,j]
    return trace
    pass
