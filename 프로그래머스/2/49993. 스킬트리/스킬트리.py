def solution(skill, skill_trees):
    answer = -1
    skillDict = dict()
    
    cnt = 0
    for ski in skill_trees:
        isPossible = True
        
        for i in range(len(skill)):
            skillDict[skill[i]] = [i, False]
        
        for j in range(len(ski)):
            temp = list(skillDict.keys())
            
            if ski[j] in temp:
                print(f'  테스트 중인 j: {ski[j]}')
                order = skillDict[ski[j]][0]
                print(f'    order: {order}')
                
                for k in list(skillDict.values()):
                    print(f'      k: {k}')
                    
                    if k[0] < order:
                        if k[1] == False:
                            isPossible = False
                            break
                    else:
                        break
                            
                skillDict[ski[j]][1] = True    
            
            if isPossible == False:
                break
        
        if isPossible:
            cnt += 1
            
        print()
            
    return cnt