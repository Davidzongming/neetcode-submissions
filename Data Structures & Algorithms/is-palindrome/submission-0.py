class Solution:
    def isPalindrome(self, s: str) -> bool:
        #use ASCII to check if the forward and backward index has the same value 
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()

        i = 0
        j = len(newStr) - 1
        for char in range(len(newStr) - 1):
            if ord(newStr[i]) != ord(newStr[j]):
                return False
            i += 1
            j -= 1
        return True
            