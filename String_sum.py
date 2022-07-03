# Python-Solution-interviewbit-
'''Question:-Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. 

Return the sum of the three integers.

Assume that there will only be one solution

Example: 

given array S = {-1 2 1 -4}, 

and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)'''


##Approach:- Simple solution can be done using nested loops and getting sum of three elements then finding the minimum or closest element but it's 
###time complexity is O(N^3). So
###Second approach using pointers 
'''1. sort the array using ny method. (I have solve using inbuilt function)
2. set some maximum range of the possible sum of the array(I had useed sum of square of element in array)
3. set two pointers low and high. then if the sum of first element in the range of for loop with the high and low term. COmpare the sum
   if it is less than B or closest check it. If sum > target then high vlaue should decrease else lower pointer should increase'''


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        A.sort()
        r=[i**2 for i in A]
        sum1=sum(r)
        
        for i in range(len(A)-2):
            low=i+1
            high=(len(A))-1
            while low<high:
                final=A[i]+A[low]+A[high]
                if abs(final-B)<abs(B- sum1):
                    sum1=final
                if final>B:
                    high-=1
                else:
                    low+=1
        return sum1
  r=Solution()
  print(r.threeSumClosest([1,2,-1,4], 1))
                    
                    
                
