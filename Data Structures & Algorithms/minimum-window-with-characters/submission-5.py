class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #a counter of size, that take the minimum size
        #we take the set of all the t, to take out the non dup values
        #one for loop will take the and check the all the letters one by one in s
        #and keep count that if all the letters are prestnt, if all are there, we thatn start again, by saving that number in the  counter abd check again, if we find the smalles after one go, we just giprint the one with the lenth of the substring starting frok that lication
        # to save the location, we can keep the starting inxex saved somewhere, and thant from the min size of the ocunter, we will start and rnt taht string from that postion to the length
        
        # a=0

        if not s or not t:
            return ""

        need=Counter(t)
        have, required=0, len(need)

        l=0
        min_start, min_len=0, float("inf")

        for r in range(len(s)):
            char=s[r]

            if char in need:
                need[char]-=1
                if need[char]==0:
                    have+=1

            while have==required:
                current_len=r-l+1

                if current_len<min_len:
                    min_start=l
                    min_len=current_len

                left_char=s[l]
                if left_char in need:
                    need[left_char]+=1

                    if need[left_char]>0:
                        have-=1
                l+=1

        return s[min_start:min_start+min_len] if min_len!=float("inf") else ""
