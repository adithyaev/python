def even_or_odd(num):
    if num == 0:
        print(f"{num} is zero")
    elif num > 0:
        if num % 2 == 0:
            print(f"{num} is even")
        else:
            print(f"{num} is odd")
    else:
        print(f"{num} is negative number")
        
# even_or_odd(2)

def check_prime(num1): # num1 = 5
    flag = False
    if num1 == 1: # F
        print(f"{num1} is not prime number")
    elif num1 > 1: # T
        for i in range(2,num1): # i = 2 | i = 3 | i = 4 .... range(2,5)
            if (num1 % i) == 0: # 5 % 2 = 1 | 5 % 3 = 2 | 5 % 4 = 1
                flag = True
                break
        if flag: # flag = F
            print(f"{num1} is not prime number") # flag = T
        else: 
            print(f"{num1} is prime number") # flag = F
            
# check_prime(2)