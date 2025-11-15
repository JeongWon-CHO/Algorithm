function solution(number) {
    const combination = new Set();
    for(let i=0; i<number.length; i++) {
        for(let j=i+1; j<number.length; j++) {
            for(let k=j+1; k<number.length; k++) {
                combination.add([number[i], number[j], number[k]].sort());
            }
        }
    }
    
    let combiSize = combination.size;
    
    let cnt = 0;
    Array.from(combination).forEach((cur) => {
        let sum = 0;
        for(let i=0; i<3; i++)
            sum += cur[i]
        
        if (sum === 0) cnt += 1;
    });
    
    return cnt;
}