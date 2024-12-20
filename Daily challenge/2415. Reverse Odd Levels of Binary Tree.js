var reverseOddLevels = function (root) {
  if (!root) return null;
  traverseDFS(root.left, root.right, 1);
  return root;
};

function traverseDFS(leftChild, rightChild, level) {
  if (!leftChild || !rightChild) return;

  if (level % 2 === 1) {
    let temp = leftChild.val;
    leftChild.val = rightChild.val;
    rightChild.val = temp;
  }

  traverseDFS(leftChild.left, rightChild.right, level + 1);
  traverseDFS(leftChild.right, rightChild.left, level + 1);
}
