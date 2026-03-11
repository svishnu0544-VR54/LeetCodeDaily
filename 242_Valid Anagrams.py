'''
Sort the version and check anagram :
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        return sorted(s)==sorted(t)
'''

'''
Using Hash Map:
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS, countT = {}, {}
        for i in range(len(s)-1):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS==countT
'''
# Using Array
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        #create a 26 size array for frequency
        frequency = [0]*26 
        for i in range(len(s)):
            frequency[ord(s[i]) - ord('a')] += 1 #ord() gives ascii value ord(a) is 97
            frequency[ord(t[i]) - ord('a')] -= 1
            
        for  i in frequency:
            if i!=0:
                return False
        return True
