n=int(input())
k=int(input())
a=list(map(int,input().split()))
max_sum=0,windowsum=0
start=0
for i in range(len(arr)):
   windowsum+=arr[i]
   if i>=k-1:
      max_sum=max(max_sum,window sum)
      window_sum-=a[start]
      start+=1
return max_sum
     
