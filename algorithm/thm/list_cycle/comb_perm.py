# combination([1,2,3,4],2) = ([1] + combination([2,3,4],1)) and
# ([2] + combination([3,4],1)) and ([3] + combination([4],1))
def comb(lst, n):

    ret = []
    if n > len(lst) : return ret

    if n == 1:
        for i in lst:
            ret.append([i])

    elif n > 1:
        for i in range(len(lst) - n + 1):
            for temp in comb(lst[i+1:], n - 1):
                ret.append([lst[i]] + temp)

    return ret

# permutation([1,2,3,4],2) = ([1] + permutation([2,3,4],1)) and
# ([2] + permutation([1,3,4],1)) and ([3] + permutation([1,2,4],1)) and
# ([4] + permutation([1,2,3],1))
def perm(lst, n):

    ret = []
    if n > lend(lst) : return ret

    if n == 1:
        for i in lsts:
            ret.append([i])

    elif n > 1:
        for i in range(len(lst)):
            temp = [i for i in lst]
            temp.remove(lst]i)
            for p in perm(temp, n - 1):
                ret.append([lst[i]] + p)

    return ret