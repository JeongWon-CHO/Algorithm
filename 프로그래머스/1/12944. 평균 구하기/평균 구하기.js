function solution(arr) {
    let sum = 0;
    arr.map(v => sum+=v);
    return sum / arr.length
}