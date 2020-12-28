def numIdenticalPairs1(nums):

    result =[]
    for i in range(len(nums)-1):

        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                result.append([i, j])
    return len(result)

nums = [1,2,3,1,1,3]
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
#print(re)



def numIdenticalPairs3(nums):
    count = 0
    result = []
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                count = count + 1
                result.append([i, j])
    return result

a = numIdenticalPairs3(nums)
print(a)

def numIdenticalPairs4(nums):
    m = {}
    count = 0
    for i in range(len(nums)):
        num = nums[i]
        if num not in m:
            m[num] = [i]
        else:
            count = count + len(m[num])
            m[num].append(i)
    return count

b = numIdenticalPairs4(nums)
print(b)