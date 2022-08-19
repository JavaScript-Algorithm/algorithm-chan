function solution(brown, yellow) {
    for (let w = 3; w < brown; w++) {
        const h = (brown - w * 2) / 2 + 2;
        if (w * h - brown === yellow) return w > h ? [w, h] : [h, w];
    }
}