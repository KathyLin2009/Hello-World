def fib(n):
    if n == 0:
        return 0
    nums = [0, 1]
    for i in range(n-1):
        third = nums[-1] + nums[-2]
        nums.append(third)
    print(nums)
    return nums[-1]
n = 0
re = fib(n)
print(re)