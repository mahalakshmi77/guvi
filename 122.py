// Given an array of N elements switch(swap) the element with the adjacent element and print the output.
Sample Testcase :
INPUT
5
3 2 1 2 3
OUTPUT
2 3 2 1 3  //

N=int(input())
arr=input()
l=list(map(int,arr.split())
for i in range (0,N)
    for j in range(i+1,N)
    tmp = arr[i]
    arr[i] = arr[i+1]
    arr[i+1] = temp
     print(arr)    
