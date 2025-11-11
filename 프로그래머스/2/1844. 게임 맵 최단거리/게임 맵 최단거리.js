const dy = [-1, 1, 0, 0];
const dx = [0, 0, 1, -1];

function OOB(y, x, n, m) {
    return y < 0 || x < 0 || y >= n || x >= m;
}

function BFS(stY, stX, board) {
    const n = board.length;
    const m = board[0].length;
    
    const q = [];
    const dist = Array.from({ length: n }, () => Array(m).fill(-1));
    
    q.push([stY, stX]);
    dist[stY][stX] = 1;
    
    while(q.length > 0) {
        const [curY, curX] = q.shift();
        
        for(let i=0; i<4; i++) {
            const ny = curY + dy[i];
            const nx = curX + dx[i];
            
            if(OOB(ny, nx, n, m))
                continue;
            if(dist[ny][nx] !== -1)
                continue;
            if(board[ny][nx] === 0)
                continue;
            
            dist[ny][nx] = dist[curY][curX] + 1;
            q.push([ny, nx]);
        }   
    }
    return dist
}

function solution(maps) {
    const dist = BFS(0, 0, maps);
    const answer = dist[maps.length-1][maps[0].length-1];
    
    return answer;
}