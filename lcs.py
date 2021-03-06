# length of longest common subsquence
# populate lcs 2d array 
# while comparing 2 str if new match is obtained add +1 to previously obtained lcs 
def lcs(str1 , str2): 
    m = len(str1) 
    n = len(str2) 
  
    L = [[0]*(n+1) for i in range(m+1)] 
  
    for i in range(m+1): 
        for j in range(n+1): 
            if i == 0 or j == 0 : 
                L[i][j] = 0
            elif str1[i-1] ==str2[j-1]: 
                L[i][j] = L[i-1][j-1]+1
            else: 
                L[i][j] = max(L[i-1][j] , L[i][j-1]) 
  
    return L[m][n] 
			
# print(lcs("axgxagxg","atatatxgax"))