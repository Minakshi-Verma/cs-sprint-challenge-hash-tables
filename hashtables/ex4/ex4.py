def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Check if there are numbers <0 in the list
    # store them in cache as negative numbers
    # Check the given list and match with cache
    # if number found return it

    cache ={}
    for number in a:
        # check for negatives
        if number < 0:
            # store them in cache as negative number
            cache[number * -1] = True
    result = []

    #Iterate through the whole list of number
    for number in a:
        # if number matches with numbers stored in cache, means it has a pair
        if number in cache:
            result.append(number) 

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
