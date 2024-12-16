var getFinalState = function (nums, k, multiplier) {
  for (let i = 0; i < k; ++i) {
    m = Math.min(...nums);
    index = nums.indexOf(m);
    nums[index] *= multiplier;
  }
  return nums;
};
