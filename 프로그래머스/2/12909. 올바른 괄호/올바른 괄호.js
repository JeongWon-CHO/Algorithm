function solution(s){
    const stack = [];
    const tmp = s.split('')
    
    tmp.forEach((v) => {
        if (stack.length === 0) stack.push(v);
        else if (stack[stack.length-1] ===')') stack.push(v);
        else {
            if (stack[stack.length-1] ==='(') {
                if (v === ')') stack.pop();
                else stack.push(v);
            }
        }
    })

    return stack.length > 0 ? false : true;
}