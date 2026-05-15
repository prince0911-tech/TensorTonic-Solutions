import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
      # Check if probabilities sum to 1.0
    if not np.isclose(np.sum(p), 1.0):
        raise ValueError("Probabilities must sum to 1.0")
        
    # Check for same length matching your test suite requirements
    if len(x) != len(p):
        raise ValueError("Inputs must have the same length")

    x=np.array(x)
    p=np.array(p)
    return float(np.sum(x * p))
    pass
