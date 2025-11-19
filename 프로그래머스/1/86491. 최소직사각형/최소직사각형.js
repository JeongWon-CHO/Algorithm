function solution(sizes) {
    const [W, H] = sizes.reduce(
        ([accW, accH], [w, h]) => 
        [Math.max(Math.max(w, h), accW), Math.max(Math.min(w, h), accH)], [0, 0]
    );
    
    return W * H;
}