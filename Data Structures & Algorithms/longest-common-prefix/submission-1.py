class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #res string 
        res=""
        #iterate the given string holding the first
        #string as the init one
        for i in range(len(strs[0])):
            #iterate each string comparing the main
            for s in strs:
                #if the string ended or doest match char, return the res
                if i==len(s) or s[i]!=strs[0][i]:
                    return res
            #add all matched string index to res
            res+=strs[0][i]
        return res
