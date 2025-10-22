function solution(n) {
    let answer = '';
    let su = '수';
    let bak = '박';
    
    for(let i=0; i<n; i++) {
        if (i % 2 === 0) answer += su;
        else answer += bak;
    }
    
    return answer;
}