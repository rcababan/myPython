# Returns first name and the initial of last name


def nametag(first_name, last_name):
    if first_name == "":
        error_msg = "Please provide your first name."
    elif last_name == "":
        error_msg = "Please provide your last name."
    elif first_name.isalpha() != True or last_name.isalpha() != True:
        error_msg = "Name should be in alphabet! Try again."
    else:
        return "Welcome! {} {[0]}.".format(first_name, last_name)
    return error_msg


print(nametag("Alex", "Handsome"))