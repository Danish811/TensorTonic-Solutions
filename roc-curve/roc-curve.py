import numpy as np

def roc_curve(y_true: list, y_score: list) -> dict:
    """
    Returns a dictionary with fpr, tpr, and thresholds.
    """
    
    curr_fpr = 0 
    curr_tpr = 0
    curr_threshold = float("inf")

    fpr = np.array([curr_fpr])
    tpr = np.array([curr_tpr])
    thresholds = np.array([curr_threshold])
    
    
    score_thresholds = np.sort(np.unique(y_score))[::-1]
    
    P = np.sum(np.array(y_true) == 1)
    N = np.sum(np.array(y_true) == 0 )
    
    for thres in score_thresholds:
        
        tpos = 0
        fpos = 0
        
        for i in range(len(y_true)):
            if y_score[i] < thres:
                continue

            if y_true[i] >= thres:
                tpos += 1
            elif y_true[i] < thres:
                fpos += 1

        
        fpr = np.append(fpr, fpos/N) 
        tpr = np.append(tpr, tpos/P)
        thresholds = np.append(thresholds, thres)
            

    return {"fpr" : fpr, "tpr" : tpr, "thresholds": thresholds}
            
 