import numpy as np

def interaction_features(X: list) -> list:

    res = []
    for row in X:
        arr = np.asarray(row)
        n = len(arr)
        i, j = np.triu_indices(n, k=1)
        interactions = arr[i] * arr[j]
        res.append(np.concatenate([arr, interactions]).tolist())
    return res