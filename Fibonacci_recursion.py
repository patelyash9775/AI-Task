
def fibonacci(n):
    if(n==1 or n==0):
        return(n)
    else:
        return(fibonacci(n-1)+fibonacci(n-2))
    
n=int((input("Enter a non-negative number :- ")))

for i in range(0,n+1):
    print(fibonacci(i))
    
    
