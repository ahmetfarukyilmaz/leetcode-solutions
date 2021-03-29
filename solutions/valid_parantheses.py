class Solution:
    def isValid(self, s):
        bool = False
        list_1 = []
        list_1[:0] = s
        for i in range(1, len(list_1)):
            if list_1[i - 1] == '(' and list_1[i] == ')':
                del list_1[i - 1:i + 1]
                bool = True
                break
            if list_1[i - 1] == '[' and list_1[i] == ']':
                del list_1[i - 1:i + 1]
                bool = True
                break

            if list_1[i - 1] == '{' and list_1[i] == '}':
                del list_1[i - 1:i + 1]
                bool = True
                break
        if not list_1:
            return True
        elif not bool:
            return False

        else:
            return self.isValid(list_1)
