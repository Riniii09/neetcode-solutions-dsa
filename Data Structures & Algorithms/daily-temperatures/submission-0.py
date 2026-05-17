class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = []
        for i in range(n):
            found = False
            for j in range(i + 1, n):
                if not found:
                    if temperatures[j] > temperatures[i]:
                        result.append(j-i)
                        found = True
            if not found:
                result.append(0)
            print("Found warmer temp: ")
            print(found)
            print("result is: ")
            print(result)
        print("Final result is: ")
        print(result)
        return result