class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        res_lst = []
        median = 0
        l1 = len(nums1)
        l2 = len(nums2)

        i = 0
        j = 0

        while i < l1 and j < l2:
            if nums1[i] < nums2[j]:
                res_lst.append(nums1[i])
                i += 1
            else:
                res_lst.append(nums2[j])
                j += 1

        res_lst += nums1[i:] + nums2[j:]

        N = len(res_lst)

        if len(res_lst) % 2 == 0:
            median = (res_lst[N // 2 - 1] + res_lst[N // 2]) / 2
        else:
            median = res_lst[N // 2]

        return median


lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
obj = Solution()
print(obj.findMedianSortedArrays(lst1, lst2))
