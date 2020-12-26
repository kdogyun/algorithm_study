class node():
    def __init__(self):
        self.child = {}
        self.finish = False

# 가능한 숫자 : 0 ~ 9
for _ in range(int(input())): # 1 ~ 50
    numbers = [input() for _ in range(int(input()))] # 1 ~ 10000
     # 전화 길이는 최대 10
    numbers.sort()
    
    result = True
    root_node = node()
    
    for number in numbers:
        check_node = root_node
        
        if result == False:
            break
        
        for num in number:
            if check_node.finish == True or result == False:
                result = False
                break
            
            if num in check_node.child.keys():
                child = check_node.child[num]
                check_node = child
            else:
                new_node = node()
                check_node.child[num] = new_node
                check_node = new_node
        check_node.finish = True
            
    if result == False:
        print('NO')
    else:
        print('YES')
