class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t_pointer = 0
        s_pointer = 0
        
        # Traverse string t until either pointer reaches the end of their respective strings
        while t_pointer < len(t) and s_pointer < len(s):
            if t[t_pointer] == s[s_pointer]:
                s_pointer += 1  # Move to the next character in s
            t_pointer += 1  # Always move to the next character in t
        
        return s_pointer == len(s)