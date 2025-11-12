function solution(d, budget) {
    let answer = 0;
    let cnt = 0;
    
    d.sort((a, b) => (a - b));

    d.forEach((v) => {
        if (budget >= (answer + v)) {
            answer += v;
            cnt += 1;
        }
    })
    
    return cnt;
}