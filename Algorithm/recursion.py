#recursion 

#print numbers recursively
def print_numbers(n):
    if n==0:
        return 
    else:
        print(n)
        print_numbers(n-1)

def sum_digit(n):
     if n == 0:
         return 0 
     else:
         return (n%10) + sum_digit(n//10)
     
def factorial(n):
    if n== 1:
        return 1
    else:
        return n * factorial(n-1)
    
def countdown(n):
    if n>0:
        print(n)
        countdown(n-1)
    else:
        return

def countup(n):
    if n== 0:
        return # return simply means the other function continues from where the recursion is called 
    else:
        countup(n-1) # it will continue from here when recursion returns
        print(n)        

def sumOfN(n):
    if n == 0 :
        return 0
    else:
        return n + sumOfN(n-1)




if __name__ == "__main__":
    # print_numbers(5)
    # print(sum_digit(1234))
    # print(factorial(10))
    countdown(5)
    print(countup(5))
    print(sumOfN(5))