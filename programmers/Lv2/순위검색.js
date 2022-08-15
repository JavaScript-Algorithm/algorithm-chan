const lowerBound = (arr, target) => {
    let left = 0;
    let right = arr.length;
    while (left < right) {
        const mid = Math.floor((left + right) / 2);

        if (arr[mid] >= target) right = mid;
        else left = mid + 1;
    }

    return left;
}

// {정보: 숫자배열} 객체 반환
const getInfos = (info) => {
    const infos = {};
    info.forEach(infoString => {
        const arr = infoString.split(" ");
        const score = parseInt(arr.pop());
        const key = arr.join("");
        if (infos[key]) infos[key].push(score)
        else infos[key] = [score];
    });

    for (const key in infos) {
        infos[key].sort((a, b) => a - b);
    }

    return infos;
}

// 쿼리별 infos 객체로 만족하는 점수 개수 반환
const getResult = (infos, query, score) => {
    const infosKey = Object.keys(infos); // key 배열

    return infosKey
        .filter(key => query.every(v => key.includes(v)))
        .reduce((acc, key) => {
            return acc + infos[key].length - lowerBound(infos[key], score);
        }, 0);
}

const solution = (info, querys) => {
    const infos = getInfos(info);

    return querys
        .map(query => {
            return query.split(/ and | |-/i)
                .filter(v => v !== "")
        })
        .map(query => {
            const score = query.pop();
            return getResult(infos, query, score);
        })
}