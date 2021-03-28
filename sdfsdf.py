def solution(program, flag_rules, commands):
    answer = []

    # rule dic 생성
    rules = ruleParse(flag_rules)

    for command in commands:
        # command별 program과 파싱 dic 생성
        command_program, command_dic = argParse(rules, command)
        # 프로그램이 동일하며, 파싱 dic에 아무 이상 없을 시 true
        if program == command_program and command_dic:
            answer.append(True)
        else:
            answer.append(False)

    return answer

# flag에 따른 arg 갯수 반환
# 2는 여러개 받을 수 있다는 의미
def checkArgNum(_type):
    if _type == 'STRING':
        return 1
    elif _type == 'NUMBER':
        return 1
    elif _type == 'STRINGS':
        return 2
    elif _type == 'NUMBERS':
        return 2
    elif _type == 'NULL':
        return 0
# flag에 따른 arg type 확인
def checkArgType(_type, arg):
    if _type == 'STRING':
        return arg.isalpha()
    elif _type == 'NUMBER':
        return arg.isdigit()
    elif _type == 'STRINGS':
        return arg.isalpha()
    elif _type == 'NUMBERS':
        return arg.isdigit()
    elif _type == 'NULL':
        return arg == ''
# rule을 dic형태로 변환
def ruleParse(flag_rules):
    rules = {}
    for rule in flag_rules:
        flag, arg = rule.split()
        rules[flag] = arg
    return rules
# command를 dic으로 변환하며
# 여러가지 상황에 대해 처리
def argParse(rules, command):
    flag = False
    parsing = {}
    command = list(command.split())
    program = command[0]
    del command[0]
    
    while command:
        key = command[0]

        # flag는 rule에 있는 것만 나타나므로 없는 것 발견 시 빈 dic 반환
        if key not in rules.keys():
            flag = True
            break
            
        # flag는 0번 혹은 1번 나타나므로 이미 존재하는 flag 발견 시 빈 dic 반환
        if key in parsing.keys():
            flag = True
            break
        
        # 해당 flag가 arg를 가지는 지 확인 후 arg 설정
        # 만약 NULL일 경우는 빈 리스트를,
        # NULL이 아닐 경우 받을 수 있는 만큼 받아서 리스트에 넣어 저장
        arg_list = []
        arg = ''
        if checkArgNum(rules[key]):
            while(True):
                try:
                    arg = command[1]
                # 만약 arg가 필요한데 더이상 리스트가 없을 때, 오류 처리 및 빈 dic 반환
                except:
                    if checkArgNum(rules[key]) == 1:
                        flag = True
                    if len(arg_list) == 0:
                        flag = True
                    break

                arg_list.append(arg)
                if checkArgNum(rules[key]) == 1:
                    if not checkArgType(rules[key], arg):
                        flag = True
                    break
                else:
                    # flag 별 type이 맞는지 확인
                    if not checkArgType(rules[key], arg):
                        print(arg)
                        del arg_list[-1]
                        break
                del command[1]
        parsing[key] = arg_list
        del command[0]
        
        if flag:
            print(1111)
            break

    print(parsing)
    if flag:
        parsing = {}
    print(parsing)
        
    return program, parsing
    

print(solution("trip", ["-days NUMBERS", "-dest STRING"], ["trip -days 15 10 -dest Seoul Paris", "trip -days 10 -dest Seoul"]))