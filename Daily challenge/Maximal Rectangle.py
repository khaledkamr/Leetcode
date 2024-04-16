class Solution(object):
    def largest_area(self, n, row_histogram):
        area = 0
        for i in range(n):
            breadth = 1
            area = max(area, row_histogram[i] * breadth)

            j = i - 1
            while j >= 0:
                if row_histogram[j] >= row_histogram[i]:
                    breadth += 1
                else:
                    break
                j -= 1

            j = i + 1
            while j < n:
                if row_histogram[j] >= row_histogram[i]:
                    breadth += 1
                else:
                    break
                j += 1

            area = max(area, row_histogram[i] * breadth)
        return area

    def maximalRectangle(self, matrix):
        area = 0
        row_histogram = [0] * len(matrix[0])

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    row_histogram[j] += 1
                else:
                    row_histogram[j] = 0
            area = max(area, self.largest_area(len(matrix[0]), row_histogram))
        return area
        