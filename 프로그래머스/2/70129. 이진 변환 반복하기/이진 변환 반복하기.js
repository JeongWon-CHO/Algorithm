function binary(x) {
    let origin = x.length;
    
    const numberOne = x.split('').filter((v) => v === '1');
    let n = numberOne.length;  // n진수
    
    let deceZero = origin- n;  // 줄어든 0의 개수
    
    if (n === 1) return ['1', deceZero];
    
    const answer = [];
    let quotient = -1;
    while (n > 1) {  // 이진변환 로직
        answer.push(n % 2);  // 나머지
        n = parseInt(n/2)  // 몫
        quotient = n; // 맨 마지막에 몫을 합쳐줘야 되니까 저장
    }
    
    let result = quotient + answer.reverse().join('');
    
    return [result, deceZero];
}

function solution(s) {
    const numberOne = s.split('').filter((v) => v === '1');
    
    let n = numberOne.length;  // n진수
    
    let cnt = 0;
    let zero = 0;
    while (s.length > 1) {
        let tmp = binary(s);
        s = tmp[0]
        zero += tmp[1]
        cnt += 1
    }
    
    return [cnt, zero];
}