#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # route= starting_ticket(source= none)--middle_tickets---ending_ticket(destination= None)
    # Check which ticket is starting ticket( source should be None)


    cache = {}
    starting_ticket = None

    #Itereate through the length of the tickets findout which ticket is starting ticket
    # for ticket in tickets:
    for i in range(length):
        ticket = tickets[i]
        if ticket.source == "NONE":
            starting_ticket = ticket
        else:
            # ticket.source is not none, store them in cache to create the route
            cache[ticket.source]= ticket

    route = [None]* length
    i= 0

    while starting_ticket is not None:        
        # if i ==length:
        #     route.append(starting_ticket)
        if i< length:                                    
            route[i] = starting_ticket.destination
        # repeat
        starting_ticket = cache.get(starting_ticket.destination)
        i +=1
    
    return route

