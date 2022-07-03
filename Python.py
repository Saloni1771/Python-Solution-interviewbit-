# Python-Solution-interviewbit-
#the questions says that There are two sorted arrays A and B of size m and n respectively.

#Find the median of the two sorted arrays ( The median of the array formed by merging both the arrays ).

#The overall run time complexity should be O(log (m+n)).

#Sample Input

'''A : [1 4 5]
B : [2 3]'''

'''Approch
1. find the final sorted array of the given two arrays 
here, using sort function --- follow the merge sort algorithms last step of merging two arrays. In mergersort the size of both arrays is same but it is different in this question So,lets check the length of both arrays first. 
2. find 
def sort(A,B):
    n=len(A)
    m=len(B)
    i=0
    j=0
    r=[]
    # if length of A is 0
    if n==0:
        return B
    #if length of B is 0
    if m==0:
        return A
    #if both of there length is non zero merge the sorted arrays
    while i<n and j<m:
        if A[i]>B[j]:
            r.append(B[j])
            j+=1
        else:
            r.append(A[i])
            i+=1
    #to append the rest of the array whose elements are yet to append
    while i<n or j<m:
      if j==m and i!=n:
        r.append(A[i])
        i+=1
      else:
        r.append(B[j])
        j+=1
        	
        
    return r
# final step to fins the median of the resultant array r            
class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def findMedianSortedArrays(self, A, B):
        x=sort(A,B)
       ## print(x)
        n=len(x)
        #print(n)
        #if size is even median= ((n/2)th +(n/2 +1)th)/2   
        if n%2==0:
            median= (x[n//2 -1]+x[n//2])/2
           # print(median)
        #or if size is odd median =n/2 th element   
        else:
            median = x[n//2]
        
        return median
x=Solution()
print(x.findMedianSortedArrays([ 1,2 ], [3,4]))

##this solution returns the median of two sorted arrays
