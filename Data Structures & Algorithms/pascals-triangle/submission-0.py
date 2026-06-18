class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for i in range(numRows):
            print("i = ", i)
            row = [1] * (i + 1)
            print("row = ", row)
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
                print("row[j] = ", row[j])
            print("row is now: ", row)
            triangle.append(row)
            print("final tri = ", triangle)
        return triangle