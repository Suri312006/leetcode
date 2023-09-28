from typing import List
class Solution:
    
    def plusOne(self, digits: List[int]) -> List[int]:
        
        pointer = len(digits)-1
        
        while digits[pointer] == 9:
            digits[pointer] = 0
            pointer -=1

        if pointer == -1:
            digits.insert(0, 1)
            
            return digits
            
        
        digits[pointer]+=1
        
        return digits
            
        
    
    
    
dig = [1,2,3]
lol = [1,2,3,5,6,9,9,4,9,9]
xd = [9]

woo = Solution()

print(woo.plusOne(dig))
print(woo.plusOne(lol))
print(woo.plusOne(xd))