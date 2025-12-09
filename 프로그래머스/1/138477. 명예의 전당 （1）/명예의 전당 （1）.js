function solution(k, score) {
    const answer = []
    const result = []
    
    for (let i=0; i<score.length; i++) {
        if (i < k) {
            answer.push(score[i]);
            answer.sort((a, b) => b - a);
        } else {
            answer.push(score[i]);
            answer.sort((a, b) => b - a);
            answer.length = k;
        }
        
        result.push(answer[answer.length-1]);
    }
    
    return result;
}