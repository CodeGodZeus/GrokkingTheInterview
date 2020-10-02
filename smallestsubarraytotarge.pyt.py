import maths                                
n=int(input())
target=int(input())
a=list(map(int,input().split()))
length=math.inf
window_sum=0
start=0
for i in range(len(a)):
    window_sum+=a[i]
    while window_sum >=target:
        length=min(length,i-start+1)
        windowsum-=a[start]
        start+=1
    return length
t.c=O(n)
s.c=O(1)


Algorithm--


This problem follows the Sliding Window pattern and we can use a similar strategy as discussed in Maximum Sum Subarray of Size K. There is one difference though: in this problem, the size of the sliding window is not fixed. Here is how we will solve this problem:

First, we will add-up elements from the beginning of the array until their sum becomes greater than or equal to ‘S’.
These elements will constitute our sliding window. We are asked to find the smallest such window having a sum greater than or equal to ‘S’. We will remember the length of this window as the smallest window so far.
After this, we will keep adding one element in the sliding window (i.e. slide the window ahead), in a stepwise fashion.
In each step, we will also try to shrink the window from the beginning. We will shrink the window until the window’s sum is smaller than ‘S’ again. This is needed as we intend to find the smallest window. This shrinking will also happen in multiple steps; in each step we will do two things:
Check if the current window length is the smallest so far, and if so, remember its length.
Subtract the first element of the window from the running sum to shrink the sliding window.
Here is the visual representation of this algorithm for the Example-1
