from __future__ import print_function


def bubble_sort(collection):
    length = len(collection)
    for i in range(length):
        swapped = False
        for j in range(length-1):
            if collection[j] > collection[j+1]:
                swapped = True
                collection[j], collection[j+1] = collection[j+1], collection[j]
        if not swapped:
            break
    return collection


if __name__ == '__main__':
    try:
        raw_input
    except NameError:
        raw_input = input

    user_input = raw_input('Enter numbers seperated by a comma: \n').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    print(bubble_sort(unsorted))

