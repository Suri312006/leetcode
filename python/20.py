class Solution:
    pairs = {
        '(':')',
        '{':'}',
        '[':']'
    }

    def isValid(self, s: str):
        
        #obvious test case
        
        if len(s)%2 != 0:
            return False
        
        opens = []
        closes = []
        
        #while loop initialization
        counter=0
        while counter < len(s):
            
            #adds char to match holder
            char = s[counter]
            
            if char in self.pairs.keys():

                opens.append(char)
                
                
            else:
                closes.append(char)
                try:
                    if self.pairs[opens[-1]] == char:
                        opens.pop(-1)
                        closes.pop()
                except IndexError:
                    return False

            counter+=1

        if len(opens) == 0 and len(closes) == 0:
            return True
        return False


woo = Solution()

print(woo.isValid(s="([}}])"))
