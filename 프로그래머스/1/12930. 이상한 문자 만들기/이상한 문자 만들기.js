function solution(s) {
    let splitString = s.split(' ');

    const answer = [];
    for (let i of splitString) {
        const tmp = i.split('');
        
        const result = tmp.map((word, idx) => {
            if (idx % 2 === 0) return word.toUpperCase();
            else return word.toLowerCase();
        });
        answer.push(result.join(''));
    }
    
    return answer.join(' ');
}