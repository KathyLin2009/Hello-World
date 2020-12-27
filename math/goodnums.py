def numIdenticalPairs1(nums):

    result =[]
    for i in range(len(nums)-1):

        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                result.append([i, j])
    return len(result)

nums = [1,2,5, 6, 7, 8, 9, 10, 3,1,1,3]
re = numIdenticalPairs1(nums)
#print(re)

def numIdenticalPairs2(nums):
    count = 0
    m = {} 
    for i in range(len(nums)):
        if nums[i] not in m:
            m[nums[i]] = [i]
        else:
            l = m[nums[i]]
            count = count + len(l)
            l.append(i)
    
    return count

re = numIdenticalPairs2(nums)
print(re)