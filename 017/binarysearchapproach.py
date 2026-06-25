def mini_day(arr,threshold):
    for i in range(1,max(arr)):
        sum=0
        for i in range(len(arr)-1):
            sum+=ceil(arr[i])