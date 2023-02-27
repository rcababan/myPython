# Returns a dictionary of how many times the letter is on the particular text.
# Key is the letter and the value is the number of times.


def countLetters(text):
    result = {}
    convertText= text.lower()
    for letter in convertText:
        if letter.isalpha() == 1:
            x = convertText.count(letter)
            result[letter] = x
    return result


print(countLetters("Math is SO Freaking fun! 2+2=4"))