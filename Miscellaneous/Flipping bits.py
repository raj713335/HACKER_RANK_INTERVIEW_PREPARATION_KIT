


for x in range(0,int(input())):
    val=int(input())
    def decimalToBinary(n):
        return "{0:b}".format(int(n))
    arr=decimalToBinary(val)
    arr=("0"*32+str(arr))[::-1]
    sum=0

    for i in range(0,32):
        
        if (arr[i]=="0"):
            sum+=(2**i)
        
    print(sum)
    
    
