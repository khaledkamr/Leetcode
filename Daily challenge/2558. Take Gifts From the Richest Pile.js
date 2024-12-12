var pickGifts = function (gifts, k) {
  let total = 0;
  for (let gift of gifts) {
    total += gift;
  }

  gifts.sort((a, b) => b - a);

  for (let i = 0; i < k; i++) {
    let largest = gifts[0];
    let new_value = Math.floor(Math.sqrt(largest));
    total -= largest - new_value;
    gifts[0] = new_value;
    gifts.sort((a, b) => b - a);
  }

  return total;
};
