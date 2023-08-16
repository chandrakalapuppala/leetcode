class Solution:
    def reverse(self, x: int) -> int:
        reverse=0
        if x>0:
            while x>0:
                reverse=reverse*10+x%10
                x= x//10
            if reverse >= 2**31-1 or reverse <= -2**31:
                return 0
            else:
                return reverse
        elif x==0:
            return 0
        elif x<0:
            x=abs(x)
            while x>0:
                reverse=reverse*10+x%10
                x=x//10
            if reverse >= 2**31-1 or reverse <= -2**31:
                return 0
            else:
                return -reverse