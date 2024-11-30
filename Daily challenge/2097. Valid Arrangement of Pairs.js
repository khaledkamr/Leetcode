var validArrangement = function (pairs) {
  const graph = new Map();
  const degree = new Map();

  for (const [x, y] of pairs) {
    if (!graph.has(x)) graph.set(x, []);
    graph.get(x).push(y);
    degree.set(x, (degree.get(x) || 0) + 1);
    degree.set(y, (degree.get(y) || 0) - 1);
  }

  let start = pairs[0][0];
  for (const [node, deg] of degree.entries()) {
    if (deg === 1) {
      start = node;
      break;
    }
  }

  const ans = [];
  const stack = [start];
  while (stack.length > 0) {
    const node = stack[stack.length - 1];
    if (graph.has(node) && graph.get(node).length > 0) {
      stack.push(graph.get(node).pop());
    } else {
      ans.push(stack.pop());
    }
  }

  ans.reverse();
  const result = [];
  for (let i = 0; i < ans.length - 1; i++) {
    result.push([ans[i], ans[i + 1]]);
  }

  return result;
};
