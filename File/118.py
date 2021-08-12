def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        
        for i in range(numRows-1):
            temp = [0]+res[-1]+[0]
            row=[]
            for j in range(len(res[-1])+1):
                row.append(temp[j]+temp[j+1])
            res.append(row)
        return res
      
      '''Explain:
      in the new row we get the previous row res[-1] and append top tail with 0[121]0 temp
      then we traverse the temp and append into the new row 1331 and go on'''
