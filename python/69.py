class Solution:
    def mySqrt(self, x: int) -> int:
        #NEED TO OPTIMIZE
        
        lol = 0

        while lol*lol <= x:
            lol+=1

        return lol-1
    
    def mySqrt1(self, x:int) -> int:

        if x < 10:
            lol = 0

            while lol*lol <= x:
                lol+=1

            return lol-1
            
        lol= int(x%10)
        
        while lol*lol <= x:
            lol+=1

        return lol-1
    
        
        
        
xd = Solution()
test = 1024
print(f'sol1: {xd.mySqrt(test)}')
print(f'sol2: {xd.mySqrt1(test)}')