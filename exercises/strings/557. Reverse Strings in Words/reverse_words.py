class Solution:
    def reverseWords(self, s: str) -> str:
        rvsd = ""
        s_list = s.split(" ")
        if len(s_list) == 0:
            return "".join(list(reversed(s)))

        for w in s_list:
            rvsd += "".join(list(reversed(w))) + " "
        return rvsd.rstrip()
