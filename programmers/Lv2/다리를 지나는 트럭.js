function solution(bridge_length, weight, truck_weights) {
    // 길이가 bridge_length 인 큐 생성
    // 1초 지날때마다 아래 수행
    // 1) pop -> 0이 아니면 sum에서 빼준다
    // 2) 다음 트럭 검사해서 unshift 할지, 0을 unshift 할지 정한다.
    const trucks_length = truck_weights.length;
    const queue = Array(bridge_length).fill(0);
    
    const arrived = [];
    let sum = 0;
    let time = 0;
    while(arrived.length !== trucks_length) {
        time++;
        const end = queue.pop();
        
        if (end !== 0) {
            sum -= end; // 합에서 빼준다
            arrived.push(end);
        }
        
        if (truck_weights[0] + sum <= weight) { 
            // 다리에 갈 수 있는 경우
            const new_truck = truck_weights.shift();
            queue.unshift(new_truck);
            sum += new_truck;            
        } else {
            queue.unshift(0);
        }
    }
    
    return time;
}