def knapSack(W, wt, val, n):
	if n == 0 or W == 0 :
		return 0
	if (wt[n-1] > W):
		return knapSack(W, wt, val, n-1)
	else:
		return max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1),
				knapSack(W, wt, val, n-1))
n,M=map(int, input().split())
Vi = []
Wi = []
for i in range(n):
    l = [int(i) for i in input().split()]
    Wi.append(l[0])
    Vi.append(l[1])    
print (knapSack(M, Wi, Vi, n))