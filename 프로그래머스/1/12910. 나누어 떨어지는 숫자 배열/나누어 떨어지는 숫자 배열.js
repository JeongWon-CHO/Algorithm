function solution(arr, divisor) {
    const answer = arr.filter((v) => (
        v % divisor === 0
    ))
    return answer.length > 0 ? answer.sort((a, b) => a-b) : [-1];
}