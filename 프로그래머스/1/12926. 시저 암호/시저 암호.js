function solution(s, n) {
    const answer = s.split('').map((v) => {
        let conversion = v.charCodeAt();  // 90 = Z  /  122 = z
        if (conversion < 65 || (90 < conversion && conversion < 97) || conversion > 122)
            return v;
        
        let result = conversion + n - 26
        
        if ((conversion <= 90) && (conversion + n > 90)) {  // 대문자 처리
            return String.fromCharCode(result)
        } else if ((conversion >= 97) && (conversion + n > 122)) {  // 소문자 처리
            return String.fromCharCode(result)
        } else return String.fromCharCode(conversion + n);
    })
    return answer.join('');
}