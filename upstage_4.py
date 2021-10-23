def count_internal_nodes(tree):
    return len(set(tree)) - 1

tree = [1, 3, 1, -1, 3]
print (count_internal_nodes(tree)) # should print 2