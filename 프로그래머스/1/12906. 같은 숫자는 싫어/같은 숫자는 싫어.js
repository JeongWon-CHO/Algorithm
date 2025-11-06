function solution(arr)
{
    const answer = [];

    let target = -1;
    arr.forEach((v) => {
        if (target !== v) {
            target = v
            return answer.push(v)
        }
    })
    
    return answer;
}