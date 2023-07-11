class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        # Need to do binary search on the smaller array in order to make it more efficient runtime
        if len(A) > len(B):
            A, B = B, A
        

        l, r = 0, len(A) - 1
        # Loop until we find a correct partition of the left side!
        while True:
            # finding the mid of A to see if it is a correct partition, then going through with binary search 
            # in order to keep trying to find the correct partition
            midA = l + ((r - l) // 2)

            # must be - 2 as total is set to the length of nums1 + nums2, thus we need to try to find the index
            midB = total - midA - 2 

            # as a checker to see if it is inbounds -> else set to -inf as a verifier to check later 
            # as a checker to see if right is inbounds -> else set to inf as a verifier to check later
            Aleft = A[midA] if midA >= 0 else float("-infinity") 
            Aright = A[midA + 1] if midA + 1 < len(A) else float("infinity")

            Bleft = B[midB] if midB >= 0 else float("-infinity")
            Bright = B[midB + 1] if midB + 1 < len(B) else float("infinity")

            
            # Case 1: It is the correct partition (ONLY one possible median)
            # Must check to see if the lefts are less than or equal to the rights because the left parition
            # will always have the smaller numbers (thats what sorted means) in non-decreasing order
            if Aleft <= Bright and Bleft <= Aright:
                # odd case, then just pick the middle
                if total % 2 == 1:
                    return min(Aright, Bright)
                
                # even case, then just take the two mid values and / 2 -> as we want a float value as the return val
                elif total % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                
            # Case 2: Aleft is greater than Bright (B has a value smaller than our current A parititon, thus it is not the correct partition)
            elif Aleft > Bright:
                r = midA - 1 # check smaller range
            else: # Bleft is greater than Aright, then B has too many values in our current left partition
                l = midA + 1

            

