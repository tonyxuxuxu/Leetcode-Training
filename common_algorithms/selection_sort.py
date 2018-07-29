from __future__ import print_function

def selection_sort(collection):

    length = len(collection)
    for i in range(length):
        least = i
        for j in range(i+1, length):
            if collection[j] < collection[least]:
                least = j
        collection[i], collection[least] = collection[least], collection[i]
    return collection


if __name__ == '__main__':
    try:
        raw_input
    except NameError:
        raw_input = input

    user_input = raw_input('Enter numbers seperated by a comma: \n').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    print(selection_sort(unsorted))