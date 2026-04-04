import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    if len(y)==0:
        return 0.0
    classes,count=np.unique(y,return_counts=True)
    prob=count/len(y)
    h=-np.sum(prob*np.log2(prob))
    return h
    pass