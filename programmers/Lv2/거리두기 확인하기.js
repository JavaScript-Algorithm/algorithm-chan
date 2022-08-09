// 유효범위 검사
const valid = (r, c) => ((r >= 0 && r < 5) && (c >= 0 && c < 5))

function check(place) {
    for (let r = 0; r < 5; r++) {
        for (let c = 0; c < 5; c++) {
            if (place[r][c] === 'P') {
                if (valid(r + 2, c) && place[r + 1][c] !== 'X' && place[r + 2][c] === 'P') return 0;
                if (valid(r - 2, c) && (place[r - 1][c] !== 'X' && place[r - 2][c] === 'P')) return 0;
                if (valid(r, c + 2) && (place[r][c + 1] !== 'X' && place[r][c + 2] === 'P')) return 0; 
                if (valid(r, c - 2) && (place[r][c - 1] !== 'X' && place[r][c - 2] === 'P')) return 0; 

                // 상하좌우 체크
                if (valid(r + 1, c) && place[r + 1][c] === 'P') return 0;
                if (valid(r - 1, c) && place[r - 1][c] === 'P') return 0;
                if (valid(r, c + 1) && place[r][c + 1] === 'P') return 0;
                if (valid(r, c - 1) && place[r][c - 1] === 'P') return 0;

                // 대각선 체크
                if (valid(r + 1, c + 1) &&
                    place[r + 1][c + 1] === 'P' && !(place[r + 1][c] === 'X' && place[r][c + 1] === 'X')) return 0;

                if (valid(r + 1, c - 1) && 
                    place[r + 1][c - 1] === 'P' && !(place[r + 1][c] === 'X' && place[r][c - 1] === 'X')) return 0;

                if (valid(r - 1, c + 1) &&
                    place[r - 1][c + 1] === 'P' && !(place[r - 1][c] === 'X' && place[r][c + 1] === 'X')) return 0;

                if (valid(r - 1, c - 1) &&
                    place[r - 1][c - 1] === 'P' && !(place[r - 1][c] === 'X' && place[r][c - 1] === 'X')) return 0;
            }
        }
    }
    
    return 1;
}

function solution(places) {
    return places.map(place => check(place));
}