class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        biggestElement = arr[n-1]

        for i in range(len(arr) - 2, -1, -1):
            element = arr[i]
            arr[i] = biggestElement
            if(biggestElement < element ):
                biggestElement = element
        arr[n-1] = -1
        return arr
