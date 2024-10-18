def solution(name, yearning, photo):
    hash = {}
    answer = []
    
    for n in range(len(name)):
        hash[name[n]] = yearning[n]
        
    # print(hash)
    
    for pho in photo:
        memory = []
        
        for p in range(len(pho)):
            score = hash.get(pho[p])
            
            if score is not None:
                memory.append(score)
            
        answer.append(sum(memory))
    
    return answer