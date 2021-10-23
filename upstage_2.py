# def find_max_sum(numbers):
#     first = max(numbers)
#     numbers.remove(first)
#     second = max(numbers)
    
#     return first + second
    
# if __name__ == "__main__":
#     print(find_max_sum([5, 9, 7, 11]))


def find_max_sum(numbers):
    second = first = -float('inf') 
    
    for num in numbers:
        if num >= first:
            second = first
            first = num
        elif second < num < first:
            second = num

    return first + second
    
if __name__ == "__main__":
    print(find_max_sum([5, 9, 7, 11]))