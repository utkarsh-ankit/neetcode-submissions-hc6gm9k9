class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Longest Substring Without Repeating Characters
        #we can have two pointers from left to right, if and we ahve a set of the unique chars
        #we both initlise by lef tand right at 0, if unique, right is hsift by one, if not, left is whift until we remove the duplicate value

        char_set=set()
        l=0
        max_len=0

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l+=1

            char_set.add(s[r])

            max_len=max(max_len,r-l+1)
        
        return max_len

