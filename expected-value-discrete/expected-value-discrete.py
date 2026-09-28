import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    arr = [1.000*x[i]*p[i] for i in range(len(x))]
    return float(sum(arr))