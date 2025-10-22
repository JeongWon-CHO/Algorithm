function factors(n) {
    let result = 0;
    for(let i=1; i<n+1; i++)
        if (n % i === 0) result += 1
    
    return result
}

function solution(left, right) {
    var answer = 0;
    for(let i=left; i<right+1; i++) 
        (factors(i) % 2 === 0) ? answer += i: answer -= i
    
    return answer;
}