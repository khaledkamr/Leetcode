<?php
class Solution {
    const N = 100001;
    private $val2H = [];
    private $removal = [];

    public function __construct() {
        $this->val2H = array_fill(0, self::N, -1);
        $this->removal = array_fill(0, self::N, -1);
    }

    private function h($root) {
        if (!$root) return -1;
        $x = $root->val;
        if ($this->val2H[$x] != -1) return $this->val2H[$x];
        return $this->val2H[$x] = 1 + max($this->h($root->left), $this->h($root->right));
    }

    private function dfs($root, $level, $maxLevel) {
        if (!$root) return;
        $x = $root->val;
        $this->removal[$x] = $maxLevel;
        $this->dfs($root->left, $level + 1, max($maxLevel, 1 + $level + $this->h($root->right)));
        $this->dfs($root->right, $level + 1, max($maxLevel, 1 + $level + $this->h($root->left)));
    }

    public function treeQueries($root, $queries) {
        $this->dfs($root, 0, 0);

        $ans = [];
        foreach ($queries as $q) {
            $ans[] = $this->removal[$q];
        }
        return $ans;
    }
}