## My example for a bulb switch problem
#You have a 1-indexed binary string of length n where all the bits are 0 initially. We will flip all the bits of this binary string (i.e., change them from 0 to 1) one by one. You are given a 1-indexed integer array flips where flips[i] indicates that the bit at index i will be flipped in the ith step.

#A binary string is prefix-aligned if, after the ith step, all the bits in the inclusive range [1, i] are ones and all the other bits are zeros.

#Return the number of times the binary string is prefix-aligned during the flipping process.
#Example 1:

#Input: flips = [3,2,4,1,5]
#Output: 2
#Explanation: The binary string is initially "00000".
#After applying step 1: The string becomes "00100", which is not prefix-aligned.
#After applying step 2: The string becomes "01100", which is not prefix-aligned.
#After applying step 3: The string becomes "01110", which is not prefix-aligned.
#After applying step 4: The string becomes "11110", which is prefix-aligned.
#After applying step 5: The string becomes "11111", which is prefix-aligned.
#We can see that the string was prefix-aligned 2 times, so we return 2.

class Solution(object):
    def numTimesAllBlue(self, flips):
        """
        :type flips: List[int]
        :rtype: int
        """
        i=0
        j=0
        prefixalligned = False
        for i in flips:
            j = flips[i] - 1
            object[j] = 1
            for s in range(1 ,flips[i]):
                if object(flips[s]-1)==1
                    prefixalligned = True
                else
                    prefixalligned = False
                    
            if prefixalligned = False:
                    print("After applying step ",i+1,": The string becomes \"",object, "which is not prefix aligned.")
      return prefixalligned
    
# Time:  O(n)
# Space: O(1)

class Solution(object):
    def numTimesAllBlue(self, light):
        """
        :type light: List[int]
        :rtype: int
        """
        result, right = 0, 0
        for i, num in enumerate(light, 1):
            right = max(right, num)
            result += (right == i)
        return result
             
