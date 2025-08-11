function solution(n) {
    n = String(n)
    var answer = [];
    for(let i=1; i<n.length+1; i++) {
        answer.push(Number(n[n.length - i]));
    }
    
    return answer;
}