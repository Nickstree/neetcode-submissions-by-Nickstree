class Solution:
    def isValid(self, s: str) -> bool:
        s_stack = []
        close_to_open = {"{":"}", "[":"]", "(":")"}
        if len(s) % 2 != 0:
            return False
        else:
            for ch in s:
                if ch in close_to_open:
                    s_stack.append(ch)
                elif len(s_stack) > 0 and ch == close_to_open[s_stack[-1]]:
                    s_stack.pop()
                else:
                    return False
        if len(s_stack) > 0:
            return False
        else:
            return True