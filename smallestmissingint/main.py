def fun(nums):
    if len(nums) > 0 and len(nums) <= 50:
        res = 0
        for i in range(len(nums)):
            if i+ 1 != len(nums) and nums[i] + 1 == nums[i+1]:
                if res > 0:
                    res += nums[i+1]
                else: res += (nums[i] + nums[i+1])
        for s in nums:
            if(res <= s):
                res = s + 1
        return res

print(fun([1,2,3,2,5]))