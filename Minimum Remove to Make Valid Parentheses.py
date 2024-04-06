class Solution(object):
    def minRemoveToMakeValid(self, s):
        string = list(s)
        count = 0

        for i in range(len(string)):
            if string[i] == '(':
                count += 1
            elif string[i] == ')':
                if count:
                    count -= 1
                else:
                    string[i] = '?'
        
        for i in range(len(string)-1, -1, -1):
            if count > 0 and string[i] == '(':
                string[i] = '?'
                count -= 1

        result = ''.join(c for c in string if c != '?')
        return result
            
        