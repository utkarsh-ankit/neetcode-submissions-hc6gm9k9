class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # two pointers coming into my mind, lets first check ofr x from both sixe ahten we shreink from the right
        # side till me find x, the we save th reange, then we shoift the l till we find a new letter
        # then we repeat the steps, and find the range of y
        # then wif we find both thre range are overlapping, we add them toghertger

        # we repeart this steps, and oif we find the new letter is out of
        # our first range, then we take the count of the old range and add int he defiend list, and thenr epeat the process

        l={}
        for i, char in enumerate(s):
            l[char]=i
        #dictionary overrites the repeating index, so it captures the alst index

        res=[]
        size=0
        end=0

        for j, char in enumerate(s):
            end=max(end, l[char])
            size+=1

            if j==end:
                res.append(size)
                size=0

        return res


        