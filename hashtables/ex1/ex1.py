#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)

# When calling hash_table_retrieve with a key that doesn't exist in the hash table, hash_table_retrieve will return None

# [4, 4], 2,8 (1,0)
# [4, 6, 10, 15, 16], 5 , 21  (3,1)
def get_indices_of_item_weights(weights, length, limit):
    # create a hashtable instance with length as the capacity
    hashtable = HashTable(length)

    # loop through weights for for an index and key
    for ndx, weight in enumerate(weights):
        # (2) check if current key(weight) is not None, returns index, value(index2)
        if hash_table_retrieve(hashtable, weight) != None:
            ndx2 = hash_table_retrieve(hashtable, weight)
            return ndx, ndx2
        else:
            # (1) inserting key(diff) and value(index), calculating diff
            diff = limit - weight
            hash_table_insert(hashtable, diff, ndx)  # 4,0

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
