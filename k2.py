# test for k = 1
def relevant_sets(n,k=2):
    SA = set() # all S(A) values that are relevant
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            # we want to add this
            if i+j <= n:
                SA.add(frozenset([i,j,i+j]))
    return SA

#SA = relevant_sets(10)

#SA = [list(x) for x in SA]
#print(SA)

# let's generate all possible colorings from [n] (by index) to {1,0}, there are 2^n
# 2d list, done using BFS
# brute force unfortunately O(2^n) (though you can't really do better)
def fill_colorings(n):
    pn = int(2**n)
    out = []
    for i in range(0,pn):
        out.append([])
    length = pn//2
    frequency = 2
    for index in range(0,n):
        val = 0
        for time in range(0,frequency):
            val = (val + 1) % 2 # 1 -> 0, 0 -> 1
            for place in range(0,length):
                out[length*time + place].append(val)
                pass
            pass
        frequency *= 2
        length = length//2
        #print(out)
        pass
    return out
#test = fill_colorings(12)
#for i in range(0,len(test)):
#    for j in range(i+1, len(test)):
#        if tuple(test[i]) == tuple(test[j]):
#            print(test[i])
#            print(test[j])
#            print('fail')

# check that a coloring is not monochromatic for a S(A)
def check_coloring(SA,coloring):
    SA = list(SA)
    color = coloring[SA[0]-1]
    for i in range(1,len(SA)):
        # non-monochromatic
        if coloring[SA[i]-1] != color:
            return True
    return False

# check that a coloring is not monochromatic for all S(A)
def check_coloring_exists(n,k=2):
    colorings = fill_colorings(n)
    SA = relevant_sets(n,k=k)
    for coloring in colorings:
        # find if a coloring exists
        exists = True
        for sa in SA:
            exists = exists and check_coloring(sa,coloring)
        # add it if we found one
        if exists:
            return True
    # we've checked every coloring and it fails
    return False

#print(check_coloring(frozenset([1,2,3]),[1,0,1])) # try switching up stuff and see it works
print(check_coloring_exists(3),3)
print(check_coloring_exists(4),4)
print(check_coloring_exists(5),5)
print(check_coloring_exists(6),6)
print(check_coloring_exists(7),7)
print(check_coloring_exists(8),8)
print(check_coloring_exists(9),9) # fails (2^9 colorings)

# let's observe
SA = relevant_sets(9)
colorings = fill_colorings(9)
SA = [list(x) for x in SA]
# for visibility, confirmed by hand
for sa in SA:
    print(sa)
print()
for coloring in colorings:
    print(coloring)

"""
\begin{lstlisting}
def relevant_sets(n,k=2):
    SA = set()
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            if i+j <= n:
                SA.add(frozenset([i,j,i+j]))
    return SA
def fill_colorings(n):
    pn = int(2**n)
    out = []
    for i in range(0,pn):
        out.append([])
    length = pn//2
    frequency = 2
    for index in range(0,n):
        val = 0
        for time in range(0,frequency):
            val = (val + 1) % 2
            for place in range(0,length):
                out[length*time + place].append(val)
                pass
            pass
        frequency *= 2
        length = length//2
        pass
    return out
def check_coloring(SA,coloring):
    SA = list(SA)
    color = coloring[SA[0]-1]
    for i in range(1,len(SA)):
        if coloring[SA[i]-1] != color:
            return True
    return False

def check_coloring_exists(n,k=2):
    colorings = fill_colorings(n)
    SA = relevant_sets(n,k=k)
    for coloring in colorings:
        exists = True
        for sa in SA:
            exists = exists and check_coloring(sa,coloring)
        if exists:
            return True
    return False
    
print(check_coloring_exists(3),3)
print(check_coloring_exists(4),4)
print(check_coloring_exists(5),5)
print(check_coloring_exists(6),6)
print(check_coloring_exists(7),7)
print(check_coloring_exists(8),8)
print(check_coloring_exists(9),9)

SA = relevant_sets(9)
colorings = fill_colorings(9)
SA = [list(x) for x in SA]
for sa in SA:
    print(sa)
print()
for coloring in colorings:
    print(coloring)
\end{lstlisting}
"""
