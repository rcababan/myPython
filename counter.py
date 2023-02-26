# Determines if it will be countdown or countup based on the 2 given numbers and returns count numbers.


def counter(start, stop):
    number_count = start
    if start > stop:
        message = "COUNTDOWN: "
        while number_count >= stop:
            message += str(number_count)
            if number_count > stop:
                message += ', '
            number_count -= 1
    else:
        message = "COUNTUP: "
        while number_count <= stop:
            message += str(number_count)
            if number_count < stop:
                message += ', '
            number_count += 1
    return message


print(counter(6, 0))
print(counter(1, 20))
print(counter(9, 9))