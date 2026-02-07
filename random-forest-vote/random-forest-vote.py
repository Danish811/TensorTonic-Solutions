def random_forest_vote(predictions):
    """
    Compute the majority vote from multiple tree predictions.
    """
    res = []
    #print("predictions are: ", predictions)

    for idx in range(len(predictions[0])):
        
        vote_counts = {}
        for v in range(len(predictions)):
            vote_counts[predictions[v][idx]] =  vote_counts.get(predictions[v][idx],0) + 1
        
        
        vote_counts = dict(sorted(vote_counts.items(), key=lambda vote_counts: vote_counts[0]))
       # print(vote_counts)

        AnsKey = list(vote_counts.keys())[0]


        for key,value in vote_counts.items():
            if value>vote_counts[AnsKey]:
                AnsKey = key

        res.append(AnsKey)
        #print("result is ", AnsKey)

    
    return res