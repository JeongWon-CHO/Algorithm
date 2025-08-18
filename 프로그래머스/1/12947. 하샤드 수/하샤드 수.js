function solution(x) {
    let strX = x + '';

    let sum = 0;
    for (let i=0; i<strX.length; i++) {
        sum += parseInt(strX[i]);
    }
    
    if (x % sum === 0) return true;
    else return false;
}