class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s[::-1].strip()
        
        
        i=0 
        while s[i] != ' ':
            i+=1
            
        return i
        
        

woo = Solution()    

woo.lengthOfLastWord("  fly me    to   the moooon  ")