import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    # Write code here
    n=len(v)
    b=np.zeros((n,n))
    for i in range(n):
                b[i,i]=v[i]
    return b       

    #return np.diag(v)
    pass
