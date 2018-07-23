from __future__ import print_function

def insertion_sort(collection):

    for i in range(len(collection)):
        while i > 0 and collection[i] < collection[i-1]:
            collection[i], collection[i-1] = collection[i-1], collection[i]
            i -= 1

    return collection

if __name__ == '__main__':
    try:
        raw_input
    except NameError:
        raw_input = input

    user_input = raw_input('Enter numbers seperated by a comma: \n').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    print(insertion_sort(unsorted))