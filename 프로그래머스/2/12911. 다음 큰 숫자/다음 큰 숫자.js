function solution(n) {
    let binaryN = n.toString(2);
    let CntbinaryN = binaryN.split('').reduce((acc, cur) => cur === '1' ? acc + 1: acc, 0);
    
    let target = n + 1;
    
    while(true) {
        let binaryTarget = target.toString(2);
        let CntbinaryTarget = binaryTarget.split('').reduce((acc, cur) => cur === '1' ? acc + 1: acc, 0);
        
        if (CntbinaryN === CntbinaryTarget) break;
        else target += 1;
    }
    return target;
}