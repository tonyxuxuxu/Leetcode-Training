from __future__ import print_function

def quick_sort(collection):

    length = len(collection)
    if length <= 1:
        return collection
    else:
        pivot = collection[0]
        smaller = [element for element in collection[1:] if element<pivot]
        greater = [element for element in collection[1:] if element>pivot]
        return quick_sort(smaller) + [pivot] + quick_sort(greater)

if __name__ == '__main__':
    try:
        raw_input
    except NameError:
        raw_input = input

    user_input = raw_input('Enter numbers seperated by a comma: \n').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    print(quick_sort(unsorted))