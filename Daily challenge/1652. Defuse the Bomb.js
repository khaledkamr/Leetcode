var decrypt = function (code, k) {
  const ans = new Array(code.length).fill(0);

  if (k === 0) {
    return ans;
  } else if (k > 0) {
    for (let i = 0; i < code.length; i++) {
      let s = 0;
      for (let j = 1; j <= k; j++) {
        s += code[(i + j) % code.length];
      }
      ans[i] = s;
    }
  } else {
    for (let i = 0; i < code.length; i++) {
      let s = 0;
      for (let j = 1; j <= -k; j++) {
        s += code[(i - j + code.length) % code.length];
      }
      ans[i] = s;
    }
  }

  return ans;
};
