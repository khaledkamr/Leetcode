var maxKDivisibleComponents = function (n, edges, values, k) {
  const adj = Array.from({ length: n }, () => new Set());
  for (const [u, v] of edges) {
    adj[u].add(v);
    adj[v].add(u);
  }
  let components = 0;
  const dfs = (node, parent = null) => {
    let sum = values[node];
    for (const u of adj[node]) {
      if (u === parent) continue;
      sum += dfs(u, node);
    }
    components += sum % k === 0 ? 1 : 0;
    return sum;
  };
  dfs(0);
  return components;
};
