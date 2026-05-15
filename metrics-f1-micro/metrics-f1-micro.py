import numpy as np

def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    # Write code here
    y_true=np.array(y_true)
    y_pred=np.array(y_pred)

    if y_true.size == 0 or y_true.shape != y_pred.shape:
        return 0.0

    # Vectorized computation of global true positives
    tp = np.sum(y_true == y_pred)
    total = y_true.size

    # In single-label multi-class, total_fp = total_fn = (total - tp)
    fp = total - tp
    fn = total - tp

    denominator = (2 * tp) + fp + fn
    if denominator == 0:
        return 0.0

    return float((2 * tp) / denominator)

  
    pass