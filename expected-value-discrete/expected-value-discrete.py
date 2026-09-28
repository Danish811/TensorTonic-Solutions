import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    exp = 0.0
    for i in range(len(x)):
        exp += x[i]*p[i]
    return exp