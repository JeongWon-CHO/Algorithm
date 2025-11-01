function solution(s) {
    let tmp = s.split(' ');
    const answer = tmp.map((e) => {
        return parseInt(e);
    })
    
    let maxValue = Math.max(...answer);
    let minValue = Math.min(...answer);
    
    console.log(maxValue)
    
    let result = `${minValue} ${maxValue}`;
    return result;
}