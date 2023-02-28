# returns a list of skipped items


data = ["a", "b", "c", "d", "e", "f", "g"]


def skip_element(elements):
    new_elements = []
    for index, element in enumerate(elements):
        i = index + 1
        if i % 2 > 0:
            new_elements.append(element)
    return new_elements


print(skip_element(data))
