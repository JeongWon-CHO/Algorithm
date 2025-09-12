function solution(phone_number) {
    let answer = '';
    for (let i=0; i<phone_number.length-4; i++) answer += '*';
    
    for (let i=4; i>0; i--)
        answer += phone_number[phone_number.length-i];
    
    return answer;
}