var maximumBeauty = function (nums, k) {
  const n = nums.length;
  let maxValue = 0;

  for (let i = 0; i < n; i++) {
    if (nums[i] > maxValue) {
      maxValue = nums[i];
    }
  }

  const range = new Array(maxValue + 10).fill(0);

  for (let i = 0; i < n; i++) {
    const left = Math.max(0, nums[i] - k);
    const right = Math.min(maxValue, nums[i] + k) + 1;
    range[left]++;
    if (right < range.length) {
      range[right]--;
    }
  }

  let result = range[0];
  for (let i = 1; i < range.length; i++) {
    range[i] += range[i - 1];
    if (range[i] > result) {
      result = range[i];
    }
  }

  return result;
};
