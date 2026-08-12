class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        a={}
        b={}
        for n in s:
            if n in a:
                a[n]+=1
            else:
                a[n]=1

        for m in t:
            if m in b:
                b[m]+=1
            else:
                b[m]=1
        return a==b
        