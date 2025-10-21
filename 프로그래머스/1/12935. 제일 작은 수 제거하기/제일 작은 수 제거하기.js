function solution(arr) {
    
    let min_num = Math.max(...arr);
    let min_num_index = -1;
    
    for(let i=0; i<arr.length; i++) {
        if (arr[i] < min_num) {
            min_num = arr[i];
            min_num_index = i;
        }
    }
    
    arr.splice(min_num_index, 1);
    
    return arr.length > 0 ? arr : [-1];
}