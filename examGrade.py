# returns the rounded percentage score and determines if it's passed or not.

def exam_grade(score, number_items):
    pass_grade = range(75, 80)
    high_grade = range(81, 90)
    top_grade = range(91, 99)
    passing_grade = 75
    if score > number_items:
        message = "The score is more than the given number of items. Please try again."
    elif score < 0:
        message = "The score is negative! That's unacceptable. Please try again."
    else:
        grade = ((score / number_items) * 100)
        if grade in pass_grade:
            message = "Your score is {}%! You passed!".format(round(grade))
        elif grade in high_grade:
            message = "Your score is {}%! Your score is high! Awesome!".format(round(grade))
        elif grade in top_grade:
            message = "Your score is {}% You got a Top Score! Amazing!".format(round(grade))
        elif grade == 100:
            message = "WOW! You got a Perfect {}% score! Dominating!".format(round(grade))
        elif grade == 0:
            message = "Oh no! You got {}%. Did you study? Try again!".format(round(grade))
        else:
            message = "Your score is {}%. You should get at least {}% to Pass. Try again.".format(round(grade), passing_grade)
    return message


print(exam_grade(7, 6))