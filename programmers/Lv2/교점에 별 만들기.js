function getIntersectPoint (A, B) {
    const [a, b, e] = A;
    const [c, d, f] = B;
    const slope = a*d - b*c;
    if (slope !== 0) {
        const x = (b*f - e*d) / slope;
        const y = (e*c - a*f) / slope; 
        return [x, y];
    }
    return [0.1, 0.1]
}

function solution(line) {
    let points = []
    
    // 1. 모든 교점 중에 정수 좌표만 구한다
    for (let i = 0; i < line.length - 1; i++) {
        for (let j = i + 1; j < line.length; j++) {
            const [x, y] = getIntersectPoint(line[i], line[j])   
            if (Number.isInteger(x) && Number.isInteger(y)) points.push([x, y]);
        }
    }
    
    // x, y의 최대, 최소 좌표를 구해준다.
    const xs = points.map(e => e[0]);
    const ys = points.map(e => e[1]);
    const [min_x, max_x] = [Math.min(...xs), Math.max(...xs)];
    const [min_y, max_y] = [Math.min(...ys), Math.max(...ys)];
        
    // 가로, 세로 길이 구해주기
    const width = max_x - min_x;
    const height = max_y - min_y;
    
    // (width+1) * (height+1) 사각형 생성후 모든 점에 별 찍어준다
    // 주의할 점은 width가 열이고, height가 행임
    const rec = Array.from({length: height + 1}, () => Array(width + 1).fill('.'));
    points.forEach(([col, row]) => rec[max_y - row][col - min_x] = '*');
    return rec.map(e => e.join(''));
}