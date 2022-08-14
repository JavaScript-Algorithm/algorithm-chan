function solution(n, t, m, timetable) {
    // n: 셔틀 운행 횟수
    // t: 셔틀 운행 간격
    // m: 셔틀버스 인원
    let ans;
    
    // 1. timetable을 먼저 분으로 바꾸고, 오름차순 정렬한다.
    timetable = timetable
                .map(time => { 
                    const [hour, min] = time.split(':').map(v => v*1);
                    return hour * 60 + min;
                })
                .sort((b, a) => b - a)
    
    // 2. 셔틀 도착 시간 배열을 만든다 - bus_time
    const bus_time = [...new Array(n)].map((_, i) => (540 + i * t))
    
    // bus_time 순회하면서 아래를 반복 - time(원소)
    bus_time.forEach((time, i) => {
        // 1) timetable에서 time보다 작은 원소들 필터링 - group
        const group = timetable.filter(e => e <= time);
        
        // 2-1) group.length > m 이면 timetable에서 앞 m개 원소 뺀다
        // 2-2) group.length <= m 이면 timetable에서 group.length개 원소 뺀다.
        if (group.length > m) timetable.splice(0, m);
        else timetable.splice(0, group.length);
        
        // 3. 마지막 time인 경우
        if (i === bus_time.length - 1) {
            // 1) group.length이 m 이상이면 group[m-1]-1 반환
            // 2) group.length가 m보다 작으면 time 반환
            ans = group.length >= m ? 
                  group[m - 1] - 1 : 
                  time
        }
        
    })
    
    return `${String(Math.floor(ans / 60)).padStart(2, '0')}:${String(ans % 60).padStart(2, '0')}`;
}