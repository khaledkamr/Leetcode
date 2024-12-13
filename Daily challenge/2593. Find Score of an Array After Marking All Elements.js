var findScore = function (nums) {
  let res = [];
  for (let i = 0; i < nums.length; i++) {
    res.push([nums[i], i]);
  }

  res.sort((a, b) => {
    if (a[0] > b[0]) {
      return -1;
    } else if (a[0] === b[0]) {
      if (a[1] > b[1]) {
        return -1;
      } else if (a[1] === b[1]) {
        return 0;
      } else {
        return 1;
      }
    } else {
      return 1;
    }
  });
  const markedIndex = new Set();

  let score = 0;
  while (res.length > 0) {
    let [smallNum, smallIndex] = res.pop();
    if (markedIndex.has(smallIndex)) {
      continue;
    }

    score += smallNum;

    if (smallIndex - 1 >= 0) markedIndex.add(smallIndex - 1);
    if (smallIndex + 1 < nums.length) markedIndex.add(smallIndex + 1);
    markedIndex.add(smallIndex);
  }

  return score;
};
