class Node {
    constructor(data, x) {
        this.data = data;
        this.x = x;
        this.left = null;
        this.right = null;
    }

    insert(data, x) {
        x <= this.x ? this._toLeft(data, x) : this._toRight(data, x);
        // 현재 값보다 작으면 왼쪽에 넣고, 크면 오른쪽에 넣는다.
    }

    _toLeft(data, x) {
        this.left ? this.left.insert(data, x) : this.left = new Node(data, x);
        // 빈 공간을 찾을 때 까지 insert 호출, null 이면 노드 생성해서 이어주기
    }

    _toRight(data, x) {
        this.right ? this.right.insert(data, x) : this.right = new Node(data, x);
        // 마찬가지로 빈 공간을 찾을 때 까지 insert 호출, null 이면 노드 생성해서 이어주기
    }
}

const postOrder = (tree, arr) => {
    if (tree != null) {
        postOrder(tree.left, arr);
        postOrder(tree.right, arr);
        arr.push(tree.data);
    }
}

const preOrder = (tree, arr) => {
    if (tree != null) {
        arr.push(tree.data);
        preOrder(tree.left, arr);
        preOrder(tree.right, arr);
    }
}

function solution(nodeinfo) {
    const nodeInfo = nodeinfo
                        .map(([a, b], idx) => [a, b, idx+1])
                        .sort((b, a) => a[1] === b[1] ? b[0] - a[0] : a[1] - b[1]);
    
    
    // [x, y, node]
    let tree;
    
    nodeInfo.forEach(([x, y, node], i) => {
        if (i === 0) {
            tree = new Node(node, x);
            return;
        }
        tree.insert(node, x);
    })
    
    const postOrderAry = [];
    const preOrderAry = [];
    postOrder(tree, postOrderAry);
    preOrder(tree, preOrderAry);
    
    return [preOrderAry, postOrderAry]
}