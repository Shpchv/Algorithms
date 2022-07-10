''' Calculate the Fibonacci number 1 <= n <= 40'''

def fib(n):
    a, b = 0, 1
    for i in range(n - 1):
        a, b = b, a + b 
        '''(a + b) % 10 change it this way for the 2 task 
        (Find the last digit of number)'''
    return b 


def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()
