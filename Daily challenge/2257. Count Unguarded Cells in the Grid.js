function dfs(r, c, dir, vis, mp) {
  const n = vis.length;
  const m = vis[0].length;

  if (r < 0 || c < 0 || r >= n || c >= m) return;
  if (mp.has(`${r},${c}`)) return;

  vis[r][c] = 1;

  if (dir === "r") {
    dfs(r, c + 1, "r", vis, mp);
  }
  if (dir === "l") {
    dfs(r, c - 1, "l", vis, mp);
  }
  if (dir === "u") {
    dfs(r - 1, c, "u", vis, mp);
  }
  if (dir === "d") {
    dfs(r + 1, c, "d", vis, mp);
  }
}

var countUnguarded = function (m, n, guards, walls) {
  const vis = Array.from({ length: m }, () => Array(n).fill(0));
  const mp = new Map();

  for (const [x, y] of guards) {
    mp.set(`${x},${y}`, 1);
    vis[x][y] = 1;
  }

  for (const [x, y] of walls) {
    mp.set(`${x},${y}`, 1);
    vis[x][y] = 1;
  }

  for (const [x, y] of guards) {
    dfs(x, y + 1, "r", vis, mp);
    dfs(x, y - 1, "l", vis, mp);
    dfs(x + 1, y, "d", vis, mp);
    dfs(x - 1, y, "u", vis, mp);
  }

  let count = 0;
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (vis[i][j] === 0) count++;
    }
  }

  return count;
};
