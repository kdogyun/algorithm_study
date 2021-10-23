from collections import defaultdict

def find_unique_numbers(numbers):
    result = []
    nums = defaultdict(int)
    
    for num in numbers:
        nums[num] += 1
        
    for key in nums:
        if nums[key] == 1:
            result.append(key)
            
    return result

if __name__ == "__main__":
    print(find_unique_numbers([1, 2, 1, 3]))