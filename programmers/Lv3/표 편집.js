// https://leego.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%91%9C-%ED%8E%B8%EC%A7%91-2021-%EC%B9%B4%EC%B9%B4%EC%98%A4-%EC%9D%B8%ED%84%B4%EC%8B%AD-JavaScript
function solution(n, k, cmd) {
    const Node = function (index, prev) {
        this.index = index;
        this.prev = prev;
        this.next = null;
    }
    
    let prevNode = new Node(0);
    let select; // 선택한 노드
    
    for(let i = 1; i < n; i++) {
        const curNode = new Node(i, prevNode);
        prevNode.next = curNode;
        prevNode = curNode;
        
        if (i === k) select = curNode;
    }
    
    const deleteBuffer = [];
    
    const moveSelectedNode = (count, direction) => {
        for (let i = 0; i < count; i++) {
            if (!select[direction]) break;
            select = select[direction];
        }
    };
    
    const deleteNode = () => {
        const { prev, next } = select;
        deleteBuffer.push(select);
        
        select = next ? next : prev;
        
        if(prev) prev.next = next;
        if(next) next.prev = prev;
    }
    
    const recoverNode = () => {
        const targetNode = deleteBuffer.pop();
        const { prev, next } = targetNode;
        
        if (prev) prev.next = targetNode;
        if (next) next.prev = targetNode;   
    }
    
    cmd
        .map(e => e.split(' '))
        .forEach(c => {
            switch (c[0]) {
                case "U":
                    moveSelectedNode(Number(c[1]), "prev");
                    break;
                case "D":
                    moveSelectedNode(Number(c[1]), "next");
                    break;
                case "C":
                    deleteNode();
                    break;
                case "Z":
                    recoverNode();
                    break;
            }
        })
    
    const result = Array(n).fill('O');
    deleteBuffer.forEach(node => {
        result[node.index] = 'X';
    })
    
    return result.join('');
}