class Solution(object):
    def divisorSubstrings(self, num, k):
        count=0
        s=str(num)
        for i in range(k,len(s)+1):
            divisor=int(s[i-k:i])
            if divisor!=0 and num%divisor==0:
                count+=1
        return count


        
        
