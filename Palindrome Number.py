class Solution(object):
    def isPalindrome(self, x):
        
        x = str(x)
        rev = x[::-1]

        if x == rev:
            return True
        else:
            return False


        