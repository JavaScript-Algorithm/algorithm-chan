function solution(citations) {  
    return citations
        .sort((b, a) => a - b)
        .filter((citation, i) => citation >= i + 1)
        .length;
}
