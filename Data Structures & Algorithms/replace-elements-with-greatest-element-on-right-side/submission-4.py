class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        # for i in range(0, n):
        #     if i == len(arr) - 1:
        #         arr[i] = -1
        #     arr[i] = max_in_array(i+1, n, arr)
        # arr[n-1] = -1
        # return arr
        max_now = arr[n-1]
        arr[n-1] = -1
        print(arr)
        for i in range(n-2, -1, -1):
            if (arr[i] <= max_now):
                print(i, max_now)
                arr[i] = max_now
            else:
                temp = arr[i]
                arr[i] = max_now
                print(i, temp, arr[i])
                max_now = temp
                print(i, max_now)
        return arr

# def max_in_array(start_pos, end_pos, arr):
#     big = 0
#     for i in range(start_pos, end_pos):
#         big = arr[i] if arr[i] > big else big
#     return big