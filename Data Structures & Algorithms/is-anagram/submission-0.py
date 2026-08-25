class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #if the strings arent equal len, false
        if len(s)!=len(t):
            return False
        #iterate the first string each char and add to a hashmap
        #hashmpa for faster lookup while comparing with 2nd str
        seen={}
        for i in s:
            if i not in seen:
                seen[i]=1
            else:
                seen[i]+=1
        #compare the saved hashmap char to 2nd word
        for c in t:
            if c in seen and seen[c]>0:
                seen[c]-=1
            else:
                return False
        #return empty hashset as true condition
        return True