class Solution:
    def isValid(self, s):
        parentheses = {"}": "{", "]": "[", ")": "("}
        result = []

        for i in s:
            if i in parentheses.values():
                result.append(i)
            elif result and parentheses[i] == result[-1]:
                result.pop()
            else:
                return False
        return result == []
