from collections import defaultdict

def nth_lowest_selling(sales, n):
    """
    :param elements: (list) List of book sales.
    :param n: (int) The n-th lowest selling element the function should return.
    :returns: (int) The n-th lowest selling book id in the book sales list.
    """
    orders = defaultdict(int)
    
    for book in sales:
        orders[book] += 1
        
    temp = []
    for key in orders:
        temp.append((orders[key], key))
    temp.sort()
    
    return temp[n-1][1]

if __name__ == "__main__":
    print(nth_lowest_selling([5, 4, 3, 2, 1, 5, 4, 3, 2, 5, 4, 3, 5, 4, 5], 2))