function solution(people, limit) {
    people.sort((b, a) => a - b);
    let [left, right] = [0, people.length - 1];
    let [sum, ans] = [people[left], 0];
    
    while (left != right) {
        if (sum + people[right] <= limit) {
            // right 태울 수 있으면 태운다 
            sum += people[right--];
        }
        else {
            // 태울 수 없으면 right 이동
            ans++;
            sum = people[++left];
        }
    }
    
    return ++ans;
}