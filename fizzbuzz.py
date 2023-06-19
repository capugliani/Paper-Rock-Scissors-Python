for number in range(1, 101):
    fizz_test = number % 3 
    buzz_test = number % 5
    if fizz_test == 0 and buzz_test == 0:
        print("FizzBuzz")
    elif fizz_test == 0:
        print("Fizz")
    elif buzz_test == 0:
        print("Buzz")
    else:
        print(number)
