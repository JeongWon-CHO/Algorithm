function solution(n, w, num) {
    
    const floor = Math.ceil(n/w);
    const storage = new Array(floor);
    
    let pos = [];
    
    let answer = 1;
    
    for (let i=0; i< floor; i++) {
        const floorArr = Array.from({ length: w }, (_, j) => (j+1) + (i*w))
        
        if (i%2 ===0) storage[i] = floorArr;
        else storage[i] = floorArr.sort((a, b) => b - a);
    }
    
    for (let i=0; i<floor; i++) {
        for (let j=0; j<w; j++) {
            if (storage[i][j] === num) pos = [i, j]
        }
    }
    
    for (const s of storage) {
        if (num < s[pos[1]] && s[pos[1]] <= n) answer += 1
    }
    
    return answer;
}