var maximumSubarraySum = function (nums, k) {
  let mp = new Map();
  let count = 0;
  let res = 0;
  let sum = 0;
  let j = 0;

  for (let i = 0; i < nums.length; i++) {
    sum += nums[i];
    mp.set(nums[i], (mp.get(nums[i]) || 0) + 1);
    if (mp.get(nums[i]) === 1) {
      count++;
    }

    if (i - j + 1 === k) {
      if (count === k) {
        res = Math.max(res, sum);
      }
      mp.set(nums[j], mp.get(nums[j]) - 1);
      if (mp.get(nums[j]) === 0) {
        count--;
      }
      sum -= nums[j];
      j++;
    }
  }

  return res;
};
