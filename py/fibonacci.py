#function to fibonacci sequence

def fibonacci(n):
   #if n is lessthan 0 it return -1
   if n == 1 and n == 0 :
       return n
   elseif n < 0:
       return -1
   else:
        return(fibonacci(n-1) + fibonacci(n-2))
