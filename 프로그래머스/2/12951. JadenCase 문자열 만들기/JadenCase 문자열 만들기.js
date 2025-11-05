function solution(s) {
    // const tmp = 'abc  dfg h';
    const words = s.split(' ');
    // console.log(words);
    const result = words.map((v) => {
        console.log(v);
        if (v === '') return ''; 
        if (/[^a-zA-Z]/.test(v[0])) return v[0] + v.slice(1,).toLowerCase();
        return v[0].toUpperCase() + v.slice(1,).toLowerCase();
    });

    return result.join(' ');
}