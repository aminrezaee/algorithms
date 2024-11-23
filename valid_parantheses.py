"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        required_stack = []
        parentheses_dict = {
            "(":")",
            "{":"}",
            "[":"]"
        }
        for char in s:
            if char not in list(parentheses_dict.keys()):
                if (len(required_stack) == 0) or (char != required_stack[-1]):
                    return False
                required_stack = required_stack[:-1]
            else: 
                required_stack.append(parentheses_dict[char])
        return len(required_stack) == 0
