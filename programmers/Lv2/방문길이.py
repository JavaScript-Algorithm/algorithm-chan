def solution(dirs):
    # from - to 해시화
    # 갈 수 있으면 가고, 갈때마다 해시에 없으면 1 증가시켜준다
    hashMap = set()
    x, y = 5, 5
    move = {'U': (-1, 0), 'D': (1, 0), 'R': (0, 1), 'L': (0, -1)}
    
    for dir in dirs:
        nx, ny = x + move[dir][0], y + move[dir][1]
        
        if 0 <= nx <= 10 and 0 <= ny <= 10:
            hashMap.add((x, y, nx, ny))
            hashMap.add((nx, ny, x, y))
            x, y = nx, ny
    
    return len(hashMap) / 2

