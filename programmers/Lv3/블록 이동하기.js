function solution(board) {
    const N = board.length;
    const goal = N + '' + N;
    const queue = [[[1, 1], [1, 2], 0]];
    const visit = new Set(["1112"]);

    const new_board = new Array(N + 2).fill().map(_ => new Array(N + 2).fill(1));
    for (let i = 0; i < N; i++) {
        for (let j = 0; j < N; j++) {
            new_board[i + 1][j + 1] = board[i][j];
        }
    }

    while (queue.length) {
        const [left, right, count] = queue.shift();

        if (left.join('') === goal || right.join('') === goal) return count;

        const nextPosition = getNextPosition(left, right, new_board);
        for (const next of nextPosition) {
            const [next_left, next_right] = next;
            const key = next_left.join('') + next_right.join('');
            if (!visit.has(key)) {
                queue.push([next_left, next_right, count + 1]);
                visit.add(key);
            }
        }
    }
}

const getNextPosition = (left, right, board) => {
    const result = [];
    
    // 1. 이동
    const moves = [[-1, 0], [1, 0], [0, -1], [0, 1]];

    for (const move of moves) {
        const [dx, dy] = move;
        const next_left = [left[0] + dx, left[1] + dy];
        const next_right = [right[0] + dx, right[1] + dy];

        if (board[next_left[0]][next_left[1]] === 0 &&
            board[next_right[0]][next_right[1]] === 0) {
            result.push([next_left, next_right]);
        }
    }

    // 2. 회전
    const toward = [-1, 1];

    // 가로 방향
    if (left[0] === right[0]) {
        for (const dx of toward) {
            if (board[left[0] + dx][left[1]] === 0 &&
                board[right[0] + dx][right[1]] === 0) {
                result.push([left, [left[0] + dx, left[1]]]);
                result.push([[right[0] + dx, right[1]], right]);
            }
        }
    }
    // 세로 방향
    else {
        for (const dy of toward) {
            if (board[left[0]][left[1] + dy] === 0 &&
                board[right[0]][right[1] + dy] === 0) {
                result.push([[left[0], left[1] + dy], left]);
                result.push([right, [right[0], right[1] + dy]]);
            }
        }
    }

    return result;
}
