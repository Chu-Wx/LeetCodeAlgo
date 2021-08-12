def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [[0]*len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        if obstacleGrid[0][0] == 0:
            dp[0][0] = 1  

        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i-1>=0:
                        dp[i][j] += dp[i-1][j]
                    if j-1>=0:
                         dp[i][j] += dp[i][j-1]
        return dp[-1][-1]
      
      
      '''[
          [0,0,0]
          [0,1,0]
          [0,0,0]
          ]
          first check if the starting value is 0 then set to one go next 
          if 1 then break 
          dp currrent value is equal to the top value plus the left value whihc is dp[i][j] = dp[i-1][j]+dp[i][j-1]
          finnaly return the last row and last col '''
