#question 6

#
#6.	Write a function that computes the list of the first 100 Fibonacci
#numbers. The first two Fibonacci numbers are 1 and 1. The n+1-st Fibonacci
#number can be computed by adding the n-th and the n-1-th Fibonacci number.
#The first few are therefore 1, 1, 1+1=2, 1+2=3,
#2+3=5, 3+5=8. Test it in your program.



#

##

def fibonacci(n):
    fib_list = [1,1]
    for i in range(2,n):
        fib_list.append(fib_list[i-1]+fib_list[i-2])
    return fib_list
print(fibonacci(100))

print(fibonacci(6))
