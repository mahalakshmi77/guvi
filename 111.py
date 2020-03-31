// Given a number N and an array of N elements ,find the Bitwise AND of the array elements.
Input Size N <= 100000
Sample Testcase :
INPUT
4
4 3 2 1
OUTPUT
0   //

def pairAndSum(arr, n) : 
    ans = 0
  
    
    for i in range(0,n) : 
        for j in range((i+1),n) : 
            ans = ans + arr[i] & arr[j] 
  
    return ans 
  

n = int(input())
arr =list(map(int,input().split())) 
print(pairAndSum(arr, n)) 
  
