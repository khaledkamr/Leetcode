var continuousSubarrays = function (nums) {
  let map = new Map();
  let start = 0;
  let end = 0;
  let res = 0;
  while (end < nums.length) {
    let num1 = nums[end];
    map.set(num1, (map.get(num1) || 0) + 1);
    end++;
    while (
      start < nums.length &&
      Math.max(...Array.from(map.keys())) -
        Math.min(...Array.from(map.keys())) >
        2
    ) {
      let num2 = nums[start];
      map.set(num2, map.get(num2) - 1);
      start++;
      if (map.get(num2) === 0) {
        map.delete(num2);
      }
    }
    let window = end - start;
    res += window;
  }

  return res;
};
