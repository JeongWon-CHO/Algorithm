function solution(s){
    var answer = true;
    
    let cnt_p = 0;
    let cnt_y = 0;
    
    let upperS = s.toUpperCase();
    
    for (let i=0; i<upperS.length; i++) {
        if (upperS[i] === 'P') cnt_p += 1;
        else if (upperS[i] === 'Y') cnt_y += 1;
    }
    
    
    return cnt_p === cnt_y ? true : false;

    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    console.log('Hello Javascript')
}