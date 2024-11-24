var maxMatrixSum = function (matrix) {
  let absSum = 0;
  let negCount = 0;
  let absMin = Infinity;

  for (const row of matrix) {
    for (const num of row) {
      absSum += Math.abs(num);
      absMin = Math.min(absMin, Math.abs(num));
      if (num < 0) negCount++;
    }
  }

  return negCount % 2 === 1 ? absSum - 2 * absMin : absSum;
};
