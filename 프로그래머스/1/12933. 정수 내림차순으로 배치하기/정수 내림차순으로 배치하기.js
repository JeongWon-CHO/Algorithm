function solution(n) {
    let strN = (n + '').split('');
    let N = strN.length;
    
    let answer = '';
    
    for (let i=0; i<N; i++) {
        let curMax = -1;
        let curIdx = -1;
        for (let j=0; j<strN.length; j++) {
            if (curMax < strN[j]) {
                curMax = strN[j];
                curIdx = j;
            }
        }
        answer += curMax;
        strN.splice(curIdx, 1);
    }
    
    return parseInt(answer);
}