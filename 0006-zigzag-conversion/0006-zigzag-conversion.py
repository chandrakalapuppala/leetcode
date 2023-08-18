class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows==1:
            return s

        rows=[[] for row in range(numRows)]   #2D array
        index=0
        step=1
        for char in s:
            rows[index].append(char)
            if index==0:
                step=1
            elif index==numRows-1:
                step=-1
            index+=step

        for i in range(numRows):
            rows[i]=''.join(rows[i])
        return''.join(rows)