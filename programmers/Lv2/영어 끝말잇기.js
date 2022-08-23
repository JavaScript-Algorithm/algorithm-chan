function solution(n, words) {
    // 중복된 단어를 말한 경우
    let notUnique = null;
    const notUniqueAry = words.filter((item, i, origin) => origin.indexOf(item) !== i);
    
    if (notUniqueAry.length) {
        const notUniqueWord = notUniqueAry.shift();
        let notUniqueIdx = words.indexOf(notUniqueWord);
        notUniqueIdx = words.indexOf(notUniqueWord, notUniqueIdx + 1);
        notUnique = [(notUniqueIdx % n) + 1, Math.ceil((notUniqueIdx + 1) / n)];
    }
    
    // 잘못된 단어를 말한 경우
    let wrongWord = null;
    for (let i = 0; i < words.length - 1; i++) {
        const [now, next] = [words[i], words[i + 1]];
        if (now[now.length - 1] !== next[0]) {
            // i + 1 번째 사람이 걸림
            wrongWord = [((i + 1) % n) + 1, Math.ceil((i + 2) / n)];
            break;
        }
    }

    // notUnique, wrongWord
    if (!notUnique && !wrongWord) return [0,0];
    return notUnique || wrongWord;
}