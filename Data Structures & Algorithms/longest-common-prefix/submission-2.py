class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=""
        #iterate the string with 1st one as base
        for i in range(len(strs[0])):
            for s in strs:
                #if the string index has ended
                #or the chars dont match end and return res
                if i==len(s) or s[i]!=strs[0][i]:
                    return res
            #add the index to the res
            res+=strs[0][i]
        return res