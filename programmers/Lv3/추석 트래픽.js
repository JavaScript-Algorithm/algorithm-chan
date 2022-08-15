function valid(start, end, val) {
    if (val >= start && val <= end) return true;
    return false;
}

function solution(lines) {
    // date sec
    // 시작: date - ms + 1ms
    // 끝: date
    
    // 구간: time ~ time + 1000ms - 1ms
    // 가능한 구간들 -> lines의 시작, 끝 값들 ~ 1초
    
    // 1. 시작과 끝 값들로 모은다
    lines = lines.map(line => {
        const [date, time, ms] = line.split(' ');
        const parsed_date = Date.parse(`${date} ${time}`);
        const parsed_ms = Number(ms.split('s')[0]) * 1000;
        return [parsed_date - parsed_ms + 1, parsed_date];
    })
    
    // 2. 가능한 구간들 모음
    // 3. 각 구간별로 개수 탐색, 최대값이 답이 된다.
    
    const check_ranges = [...new Set(lines.flat().sort())]
        .map(time => [time, time + 1000 - 1])
        .map(([start, end]) => {
            return lines
                    .filter(([s, e]) => valid(start, end, s) || 
                                        valid(start, end, e) || 
                                        valid(s, e, start) || 
                                        valid(s, e, end))
                    .length;
        });
    
    return Math.max(...check_ranges)
}