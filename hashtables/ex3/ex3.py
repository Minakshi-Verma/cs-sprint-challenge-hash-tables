def intersection(arrays):
    """
    YOUR CODE HERE
    """
    
    min_array = arrays[0]
    # print(min_arr)
    longest_length = 0
    # iterate through input array and check the min and max lengths
    for array in arrays:
        if len(min_array) > len(array):
            min_array = array           
        if len(array) > longest_length:
            longest_length = len(array)

    cache = {}
    for number in min_array:
        # store the value in cache ( as a key) to compare
        cache[number] = 0
        # print(cache)

    for i in range(longest_length):
        for array in arrays:
            if i < len(array) and array[i] in cache:
                cache[array[i]] += 1
                # print(cache)
               
            
    result = []
    # iterate through the cache dictionary using .keys()
    for key in cache.keys():       
        if cache[key] == len(arrays):
            # print(cache[key])  
            result.append(key)
            # print(result)

    return result


if __name__ == "__main__":
    arrays = []

    # arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    # arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    # arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])
    arrays.append(list(range(100, 150)) + [1, 2, 3, 4])
    arrays.append(list(range(150, 200)) + [1, 2, 3, 4, 5])
    arrays.append(list(range(250, 300)) + [1, 2, 3, 4, 8, 9])

    print(intersection(arrays))
