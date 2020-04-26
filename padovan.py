# Program to find nth term in Padovan Sequence using Dynamic Programming 

def pad(n): 
    # P0,P1,P2 = 1
    # P(n) = P(n-2) + P(n-3)
    pPrevPrev, pPrev, pCurr, pNext = 1, 1, 1, 1
  
    for i in range(3, n+1): 
        pNext = pPrevPrev + pPrev 
        # print(pNext) Uncomment to print all no.s in sequence
        pPrevPrev = pPrev 
        pPrev = pCurr 
        pCurr = pNext 
  
    return pNext

print(pad(13))