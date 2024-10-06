class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        str1 = strs[0]
        str2  = strs[-1]
        st = ""
        for i in range(min(len(str1), len(str2))):
            if str1[i] == str2[i]:
                st += str1[i]
            else:
                return st
        return st

        