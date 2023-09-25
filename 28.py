class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack): return -1
        
        if len(needle) == len(haystack):
            if needle == haystack:
                return 0
            return -1

    
        index = 0
        
        diff = len(haystack)-len(needle)

        while index <= diff:
            print(haystack[index:index+len(needle)])
            if needle == haystack[index:index+len(needle)]:

                return index
            index+=1
        
        return -1
    
woo = Solution()

print(woo.strStr(haystack="abc", needle="c"))