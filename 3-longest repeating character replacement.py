class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        size = len(s)
        if size < 2:
            return 1
        maxLen = 0
        left = 0 
        right = 1
        leftCount = 0
        rightCount = 0
        leftRightCount =0
        while right < size:
            if s[right] != s[left]:
                rightCount += 1
                if rightCount == k:
                    maxLen = max(maxLen,leftRightCount+rightCount+leftCount)
                    left += 1
                    leftCount = rightCount
                    rightCount = leftRightCount 
                    leftRightCount = 0
            else:
                if rightCount != leftRightCount:
                    leftCount += 1
                else:
                    leftRightCount += 1
                right += 1
                
        
