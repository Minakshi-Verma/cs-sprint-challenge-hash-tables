
def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    #weight = [5, 10, 15, 20, 30]
    #length= 5
    #limit= 30
    # Output = (3,1)
    #check (limit-weight) for each item in cache
    cache ={}
    for i in range(length):
        if limit-weights[i] in cache:
            # if yes, return the index tuple   
            return [i, cache[limit-weights[i]]]
        else: 
            print(cache)
            # if not--add to cache
            cache[weights[i]] = i

    return None
