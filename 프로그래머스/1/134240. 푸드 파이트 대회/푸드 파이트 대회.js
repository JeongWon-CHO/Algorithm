function solution(food) {
    const answer = [];
    for(let i=1; i<food.length; i++) {
        if (parseInt(food[i] / 2) > 0) {
            for(let j=0; j<parseInt(food[i] / 2); j++) answer.push(i);
        }
    }
    return answer.join('') + 0 + answer.reverse().join('');
}