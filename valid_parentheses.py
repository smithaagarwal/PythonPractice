""""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

"""

class Solution:

    def isValidMod(self, s: str) -> bool:
        opening_brace_list = ["{","[","("]
        closing_brace_list = ["}", "]", ")"]
        check_brace_list = list()
        for brace in s:
            if brace in opening_brace_list:
                check_brace_list.append(brace)
               # print(check_brace_list)
            elif brace in closing_brace_list:
                if len(check_brace_list) > 0:
                    p = check_brace_list.pop()
                    if (closing_brace_list.index(brace)) != (opening_brace_list.index(p)):
                        return False
                else:
                    return False
        else:
            if len(check_brace_list) > 0:
                return False
        return True


    def isValid(self, s: str) -> bool:
        opening_brace_list = ["{","[","("]
        closing_brace_list = ["}", "]", ")"]
        check_brace_list = list()
        for brace in s:
            if brace in opening_brace_list:
                check_brace_list.append(brace)
               # print(check_brace_list)
            elif brace in closing_brace_list:
                if (len(check_brace_list)>0) and ((closing_brace_list.index(brace)) == (opening_brace_list.index(check_brace_list[-1]))):
                    check_brace_list.pop()
                else:
                    return False
        else:
            if len(check_brace_list) > 0:
                return False
        return True

s = Solution()
input_str = "{[()]}"
print(s.isValidMod(input_str))

