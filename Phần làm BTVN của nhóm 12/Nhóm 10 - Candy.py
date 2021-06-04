class Solution:
    def candy(self, ratings: List[int]) -> int:
        if not ratings: return 0
        n = len(ratings)
        res = [1]*n   # minimum 1 for each
        i = 1
        while i < n:
            if ratings[i-1] > ratings[i]:
                # check whether needed to add candy to current child
                # based on right neighbor
                r = i
                while r < n and ratings[r-1] > ratings[r]:
                    for j in range(i, r): res[j-1] += 1
                i = r
            else:
                # add candy to current child based on left neighbor
                if ratings[i-1] < ratings[i] and res[i-1] >= res[i]: res[i] = res[i-1] + 1
                i += 1
        print(res)