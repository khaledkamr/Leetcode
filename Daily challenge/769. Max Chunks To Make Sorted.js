var maxChunksToSorted = function (arr) {
  let runningSum = 0,
    expectedSum = 0,
    chunks = 0;
  for (let i = 0; i < arr.length; i++) {
    runningSum += arr[i];
    expectedSum += i;
    if (runningSum === expectedSum) {
      chunks++;
    }
  }
  return chunks;
};
