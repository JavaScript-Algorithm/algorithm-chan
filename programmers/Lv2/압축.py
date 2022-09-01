def solution(msg):
    # 현재입력 cur, 다음 글자 next
    # {단어: 색인} 사전 생성
    # 1. 현재 입력에서부터 차례대로 사전에 등록된 단어 탐색 cur-next
    # 2. msg[cur:next] 가 사전에 없으면 등록
    # 3. cur = next
    # 위 과정을 next가 마지막 인덱스일때까지 반복
    
    init = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    wordIndex = { word: index+1 for index, word in enumerate(init) }
    
    if len(msg) == 1: 
        return [wordIndex[msg]]
    
    cur, nxt, index = 0, 1, 27
    ans = []
    
    while nxt != len(msg)+1:
        if msg[cur:nxt] not in wordIndex:
            ans.append(wordIndex[msg[cur:nxt-1]]) # 출력
            wordIndex.setdefault(msg[cur:nxt], index) # 사전 추가
            index += 1
            cur = nxt - 1
            continue
        nxt += 1
    
    
    # msg[cur:nxt-1] 인덱스만 추가
    ans.append(wordIndex[msg[cur:nxt-1]])
    
    return ans
        
        
    
    
    