def getLength(time1, time2):
    hour1, minute1 = map(int, time1.split(':'))
    hour2, minute2 = map(int, time2.split(':'))
    return (hour2 * 60 + minute2) - (hour1 * 60 + minute1)

def transMelody(info):
    info = info.replace('C#', 'c').replace('D#', 'd').replace('A#', 'a')
    info = info.replace('F#', 'f').replace('G#', 'g')
    return info

def mapMusicinfos(musicinfos):
    time1, time2, title, melody = musicinfos
    melodyLen = getLength(time1, time2)
    melody = transMelody(melody)
    newMelody = melody * 1440
    return [title, newMelody[:melodyLen], melodyLen]

def solution(m, musicinfos):
    # 음악이 시작한 시각, 끝난 시각, 음악 제목, 악보 정보
    # C#-Y, D#-U, F#-I, G#-O, A#-P
    musicinfos = list(map(lambda x: x.split(','), musicinfos))
    musicinfos = list(map(mapMusicinfos, musicinfos))
    m = transMelody(m)
    ans = []
    
    for title, melody, melodyLen in musicinfos:
        if melody.find(m) != -1:
            ans.append([title, melodyLen])
    
    if len(ans) == 0:
        return "(None)"
    
    ans = sorted(ans, key=lambda x: x[1], reverse=True)
    return ans[0][0]