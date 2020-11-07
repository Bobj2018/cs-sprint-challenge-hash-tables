def get_indices_of_item_weights(weights, length, limit):
    hash_table = {}
    result = []

    #store the weight as keys and the index as values
    for i in range(length):
        hash_table[weights[i]] = i

    for weight in weights:
        if (limit - weight) in hash_table:
            result.append(hash_table[limit - weight])

    if len(result) == 0:
        return None
    else:
        result.sort(reverse=True)
        return result


x = get_indices_of_item_weights([ 4, 6, 10, 15, 16 ], 5, 21)
print(x)
