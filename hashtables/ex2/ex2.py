#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

# We can hash each ticket such that the starting location is the key and the destination is the value. Then,
# when constructing the entire route, the ith location in the route can be found by checking the hash table for the i-1th location.
def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * (length - 1)

    # store ticket in hashtable (key:departure, value:destination)
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    # starting location key is NONE
    departure = "NONE"
    ndx = 0
    while hash_table_retrieve(hashtable, departure) != "NONE":
        destination = hash_table_retrieve(hashtable, departure)
        route[ndx] = destination
        departure = destination
        ndx += 1

    return route

# ticket_1 = Ticket("NONE", "PDX")
# ticket_2 = Ticket("PDX", "DCA")
# ticket_3 = Ticket("DCA", "NONE")
#
# tickets = [ticket_1, ticket_2, ticket_3]
#
# # expected = ["PDX", "DCA"]
# result = reconstruct_trip(tickets, 3)
# print(result)
