function solution(t, p) {
    let cnt = 0;
    
    for(let i = 0; i < t.length - p.length + 1; i++) {
        let sliceT = parseInt(t.slice(i, i+p.length))
        if (sliceT <= parseInt(p)) cnt += 1;
    }
    
    return cnt;
}