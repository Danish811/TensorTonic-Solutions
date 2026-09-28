import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    a = np.asarray(a, dtype='float32')
    b = np.asarray(b, dtype='float32')
    e_a = np.linalg.norm(a) 
    e_b = np.linalg.norm(b)
    if e_a == 0 or  e_b == 0:
        return 0.0
    res =  np.dot(a, b) / (e_a*e_b)
    
    return float(res)