def pattern(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end=" ")
        for j in range(0,2*i+1):
                if j==0  or j==2*i:
                    print("*",end=" ")
                else:
                     print(" ",end=" ")
        for j in range(n-i-1):
            print(" ",end=" ")
        
        print()
    return
def pattern1(n):
    for i in range(n):
        
        # leading spaces
        for j in range(i):
            print(" ", end=" ")
        
        # stars and inner spaces
        for j in range(2*(n-i)):
            if j == 0 or j == 2*(n-i)-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        
        print()  
# this must be inside outer loop
pattern(4)
pattern1(3) 

        

