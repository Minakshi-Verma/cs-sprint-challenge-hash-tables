# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    
    cache = {}

    for query in queries:
        #Add the query to the cache
        cache[query] = True
    
    result = []
    # Iterarte through all the files and see if query word in there
    for file in files: 
        # open the file and match each word separetd by "/" with cache
        if file.rsplit("/", 1)[-1] in cache:         
            # if found, append to result list
            result.append(file)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
