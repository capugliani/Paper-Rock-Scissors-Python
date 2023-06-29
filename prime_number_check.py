
#You need to write a function that checks whether if the number passed into it is a prime number or not.
def prime_checker(number):
    prime = True
    if number < 2:
        prime = False
    for numbers in range(3, number, 2):
        if number % numbers == 0:
            prime = False

    if prime == False:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)
