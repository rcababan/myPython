# returns the sum of divisors of the given number.


def total_divisors(number):
    divisor = 1
    sum = 0
    if number != 0:
        while divisor != number:
            if number % divisor == 0:
                sum += divisor
            divisor += 1
        message = "The sum of the divisors of {} is {}.".format(number, sum)
    else:
        message = "The number is {}! Can't do anything about it. Please try again.".format(number)
    return message


print(total_divisors(0))