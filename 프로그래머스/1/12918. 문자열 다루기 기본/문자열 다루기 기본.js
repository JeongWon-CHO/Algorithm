function solution(s) {
    for(let i=0; i<s.length; i++) {
        if (isNaN(s[i])) return false;
    }
    
    if (!(s.length === 4 || s.length === 6)) return false;
    return true
}