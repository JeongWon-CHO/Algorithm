function collatz(n, cnt) {
    if (n === 1) return cnt;
    
    if (cnt === 500) return -1;
    
    if (n % 2 === 0)
        return collatz(n/2, cnt+1);
    
    else if (n % 2 !== 0)
         return collatz(n*3+1, cnt+1);
}

function solution(num) {
    let cnt = 0;
    let answer = collatz(num, cnt);
    
    return answer;
}