function GCD(a, b) {  // 최대공약수
    while(b !== 0) {
        let r = a % b;
        a = b;
        b = r;
    }
    
    return a;
}

function LCM(a, b) {  // 최소공배수
    return (a * b) / GCD(a, b);
}

function solution(n, m) {
    let gcd = GCD(n, m);
    let lcm = LCM(n, m);
    
    return [gcd, lcm];
}