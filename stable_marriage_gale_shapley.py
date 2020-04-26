# Stable Marriage Problem
# Iterative Improvement Problem
# Gale-Shapley Algorithm
# Time Complexity : TODO
N = int(input())
mp=[]
mp2=[]
wp=[]
wp2=[]

for i in range(N):
    mp.append(list(map(int,input().split())))
for i in range(N):
    wp.append(list(map(int,input().split())))

for i in range(len(mp)):
    li=[]
        
    for j in range(len(mp)):
        ind = mp[i].index(min(mp[i]))
        mp[i][ind]=99
        li.append(ind+1)
    mp2.append(li)

for i in [[wp[j][i] for j in range(len(wp))] for i in range(len(wp[0]))]:
     li=[]
     for j in range(len(mp)):
        ind = i.index(min(i))
        i[ind]=99
        li.append(ind+1)
     mp2.append(li)


def higher(prefer, w, m, m1): 
    print(prefer)
    for i in range(N): 
        if (prefer[w][i] == m1): 
            return True
        if (prefer[w][i] == m): 
            return False

def stableMarriage(prefer,qu): 
    myd={}
    wPartner = [-1 for i in range(N)] 
    mFree = [False for i in range(N)]   
    freeCount = N 
  
    while (freeCount > 0): 
          
        m = 0
        while (m < N): 
            if (mFree[m] == False): 
                break
            m += 1
  
        i = 0
        while i < N and mFree[m] == False: 
            w = prefer[m][i] 
  
            if (wPartner[w - N] == -1): 
                wPartner[w - N] = m 
                mFree[m] = True
                freeCount -= 1
                try:
                    myd[w]+=1
                except:
                    myd[w]=1
            else:  
                  
                m1 = wPartner[w - N] 
                myd[w]+=1
                if (higher(prefer, w, m, m1) == False): 
                    wPartner[w - N] = m 
                    mFree[m] = True
                    mFree[m1] = False

            i += 1
  
    print(myd)

q=int(input())
for _ in range(q):
    x=int(input())
    stableMarriage(mp2,x)
