def T(nums):
    n = len(nums)
    if n < 3:
        return []
    i = 0
    nums.sort()
    if nums[0] > 0:
        return []
    res = []
    for i in range(n):
        if (i>0 and nums[i] == nums[i-1]):
            continue
        L = i + 1
        R = n - 1
        while L < R:
            if (nums[i] + nums[L] + nums[R] == 0):
                res.append([nums[i], nums[L], nums[R]])
                while L<R and nums[L] == nums[L+1]:
                    L += 1
                while L<R and nums[R] == nums[R-1]:
                    R -= 1
                L += 1
                R -= 1
            
            elif (nums[i] + nums[L] + nums[R] > 0):
                R -= 1
            else:
                L += 1
    return res


if __name__ == '__main__':
    a = [2,5,6,-7,-1,-3,-5,-4,8,3]
    print(T(a))
    