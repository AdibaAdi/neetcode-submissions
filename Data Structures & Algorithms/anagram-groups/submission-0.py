class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #res list as adjacency list to map words
        res=defaultdict(list)
        #iterate the string for words
        for w in strs:
            #count array to store char index
            #26 chars of letter 26 index(+1)
            count=[0]*26
            #iterate the word to get char index
            for c in w:
                #store the char index count
                #extract the char using ord ascii val
                #comparing against a's acsii
                #+1 as indexed are 0ed
                count[ord(c)-ord("a")]+=1
            #store the char as key val as tuple to res
            #tuple(count)= fully is key of dict for that word
            #adding that array map to the word
            res[tuple(count)].append(w)
        #return the result as list from adjacnecy list
        #this returns are values as list together in main res
        return list(res.values())