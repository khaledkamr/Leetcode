/**
 * @param {number[][]} grid
 * @return {number}
 */
var minimumObstacles = function (grid) {
  const m = grid.length;
  const n = grid[0].length;
  const directions = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0],
  ];

  const heap = new MinHeap();
  heap.push([0, 0, 0]);

  const visited = Array.from({ length: m }, () => Array(n).fill(Infinity));
  visited[0][0] = 0;

  while (!heap.isEmpty()) {
    const [obstaclesRemoved, x, y] = heap.pop();

    if (x === m - 1 && y === n - 1) {
      return obstaclesRemoved;
    }

    for (const [dx, dy] of directions) {
      const nx = x + dx;
      const ny = y + dy;

      if (nx >= 0 && nx < m && ny >= 0 && ny < n) {
        const newObstacles = obstaclesRemoved + grid[nx][ny];
        if (newObstacles < visited[nx][ny]) {
          visited[nx][ny] = newObstacles;
          heap.push([newObstacles, nx, ny]);
        }
      }
    }
  }

  return -1;
};

class MinHeap {
  constructor() {
    this.heap = [];
  }

  push(val) {
    this.heap.push(val);
    this._heapifyUp();
  }

  pop() {
    if (this.heap.length === 1) return this.heap.pop();
    const top = this.heap[0];
    this.heap[0] = this.heap.pop();
    this._heapifyDown();
    return top;
  }

  isEmpty() {
    return this.heap.length === 0;
  }

  _heapifyUp() {
    let idx = this.heap.length - 1;
    while (idx > 0) {
      const parentIdx = Math.floor((idx - 1) / 2);
      if (this.heap[parentIdx][0] <= this.heap[idx][0]) break;
      [this.heap[parentIdx], this.heap[idx]] = [
        this.heap[idx],
        this.heap[parentIdx],
      ];
      idx = parentIdx;
    }
  }

  _heapifyDown() {
    let idx = 0;
    const length = this.heap.length;
    while (true) {
      const leftIdx = 2 * idx + 1;
      const rightIdx = 2 * idx + 2;
      let smallest = idx;

      if (leftIdx < length && this.heap[leftIdx][0] < this.heap[smallest][0]) {
        smallest = leftIdx;
      }
      if (
        rightIdx < length &&
        this.heap[rightIdx][0] < this.heap[smallest][0]
      ) {
        smallest = rightIdx;
      }
      if (smallest === idx) break;
      [this.heap[smallest], this.heap[idx]] = [
        this.heap[idx],
        this.heap[smallest],
      ];
      idx = smallest;
    }
  }
}
