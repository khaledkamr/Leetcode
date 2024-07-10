class Solution:
    def minOperations(self, logs: List[str]) -> int:
        layers = 0
        for op in logs:
            if op == "../":
                layers -= 1 if layers > 0 else 0
            elif op != "./":
                layers += 1

        return layers
