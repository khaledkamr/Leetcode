var checkIfExist = function (arr) {
  const seen = new Map();

  for (const num of arr) {
    if (seen.has(2 * num) || (num % 2 === 0 && seen.has(num / 2))) {
      return true;
    }
    seen.set(num, (seen.get(num) || 0) + 1);
  }

  return false;
};
