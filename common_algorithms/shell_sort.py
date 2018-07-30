from __future__ import print_function

def shell_sort(collection):

    # length = len(collection)
    # gap = int(length/2)
    #
    # while gap > 0:
    #     for i in range(gap, length):
    #         temp = collection[i]
    #         j = i
    #         while j >= gap and collection[j - gap] > temp:
    #             collection[j] = collection[j - gap]
    #             j -= gap
    #
    #         collection[j] = temp
    # gap /= 2
    # return collection
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]

    for gap in gaps:
        i = gap
        while i < len(collection):
            temp = collection[i]
            j = i
            while j >= gap and collection[j - gap] > temp:
                collection[j] = collection[j - gap]
                j -= gap
            collection[j] = temp
            i += 1

    return collection

if __name__ == '__main__':
    try:
        raw_input
    except NameError:
        raw_input = input

    user_input = raw_input('Enter numbers seperated by a comma: \n').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    print(shell_sort(unsorted))