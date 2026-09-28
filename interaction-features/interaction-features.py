def interaction_features(X: list) -> list:
    """
    Returns original features followed by unique pairwise products.
    """
    import numpy as np

    #X = np.asarray(X)
    resList = []
    for arr in X:
        newList = arr[:]
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                res = arr[i]*arr[j]
                newList.append(res)
                
        resList.append(newList)
    print(resList)
    return resList