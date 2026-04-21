class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        f={}
        l=0
        m_l=0
        m_f=0

        for r in range(len(s)):
            f[s[r]]=f.get(s[r],0)+1
            m_f=max(m_f,f[s[r]])

            w_len=r-l+1

            if w_len-m_f>k:
                f[s[l]]-=1
                l+=1
            else:
                m_l=max(m_l,w_len)
        return m_l









        