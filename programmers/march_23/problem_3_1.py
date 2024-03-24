result=[0,0]

def compression(a,b,l,arr):
    global result
    start=arr[a][b]
    for i in range(a,a+l):
        for j in range(b,b+l):
            if arr[i][j]!=start:
                l=l//2
                compression(a,b,l,arr)
                compression(a,b+l,l,arr)
                compression(a+l,b,l,arr)
                compression(a+l,b+l,l,arr)
                return

    result[start]+=1

def solution(arr):
    global result
    length=len(arr)
        
    compression(0,0,length,arr)
    
    return (result)
