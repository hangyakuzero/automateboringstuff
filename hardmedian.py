def findmedian(nums1, nums2):
    def median(l):
        l.sort()
        n = len(l)
        if n % 2 == 1:
            return float(l[n // 2])
        else:
            return (l[n // 2 - 1] + l[n // 2]) / 2.0

    nums = nums1 + nums2
    return median(nums)


nums1 = [4, 5, 6]
nums2 = [3, 2, 1]
print(findmedian(nums1, nums2))
