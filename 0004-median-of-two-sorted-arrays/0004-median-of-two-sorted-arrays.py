class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num1_leng=len(nums1)
        num2_leng=len(nums2)
        total_leng=num1_leng+num2_leng
        median_ind=total_leng//2
        previous_value=0
        current_value=0
        num1_ind=0
        num2_ind=0
        mixed_ind=0
        while mixed_ind<=median_ind:
            previous_value=current_value
            #check if there are left elements in both arrays
            if num1_ind<num1_leng and num2_ind<num2_leng:
                if nums1[num1_ind]<nums2[num2_ind]:
                    current_value=nums1[num1_ind]
                    num1_ind+=1
                else:
                    current_value=nums2[num2_ind]
                    num2_ind+=1
            #if there are left elements in first array
            elif num1_ind<num1_leng:
                current_value=nums1[num1_ind]
                num1_ind+=1
                #if there are no elements in first array and left in second array
            else:
                current_value=nums2[num2_ind]
                num2_ind+=1
            mixed_ind+=1
            #check if the lenth of total list is even or odd
        if total_leng%2==0:
            return (previous_value+current_value)/2
        else:
            return(current_value)
            