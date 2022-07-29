function solution(records) {
    // [uid : 이름] map 생성
    // 가장 마지막 uid 이름이 본인 이름
    const uid_name = {};
    records.forEach((record) => {
        const [type, uid, name] = record.split(' ');
        if (type !== 'Leave') uid_name[uid] = name; 
    })
    
    // 출력
    const ans = []
    records.forEach((record) => {
        const [type, uid, name] = record.split(' ');
        if (type === 'Enter') ans.push(`${uid_name[uid]}님이 들어왔습니다.`)
        if (type === 'Leave') ans.push(`${uid_name[uid]}님이 나갔습니다.`)
    })
    return ans;
}