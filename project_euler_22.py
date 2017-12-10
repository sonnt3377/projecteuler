"""
    Project Euler 22: Name scores

    Using project_euler_22.txt, a 46K text file containing over five-thousand first names.
    Begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,
    multiply this value by its alphabetical position in the list to obtain a name score.

    For example, when the list is sorted into alphabetical order,
    COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
    So, COLIN would obtain a score of 938 x 53 = 49714.

    What is the total of all the name scores in the file?
"""
import time

def read_data_from_file(file_name):
    '''
    Read input data from file, and return a list containing all names

    :param file_name: input data file
    :return: list of names
    '''
    f = open(file_name)
    name_list = f.read().replace('\"', '').split(",")

    return name_list

def bubble_sort_names(name_list):
    """
    Sort list of name based on alphabetical order using bubble sort

    :param name_list: list of names
    :return: list of sorted names
    """
    for index in range(len(name_list)-1, 0, -1):
        for i in range(index):
            if name_list[i] > name_list[i+1]:
                temp = name_list[i]
                name_list[i] = name_list[i + 1]
                name_list[i + 1] = temp

def quick_sort_names(name_list):
    """
    Sort list of names based on alphabetical order using quick sort

    :param name_list: list of names
    :return: the sorted list
    """
    quick_sort_helper(name_list, 0, len(name_list) - 1)

def quick_sort_helper(list, first, last):
    """
    Sort list of names based on alphabetical order using quick sort
    Ref: https://interactivepython.org/runestone/static/pythonds/SortSearch/TheQuickSort.html

    :param list: list to be sorted
    :param first: index of the first item
    :param last: index of the last item
    :return: the sorted list
    """
    if first < last:
        pivot_point = partition(list, first, last)
        quick_sort_helper(list, first, pivot_point - 1)
        quick_sort_helper(list, pivot_point + 1, last)

def partition(list, first, last):
    """
    Partition the list into two parts, separated by the list's first item.
    The left part of this list contains all items less than the first item,
    while the right part contains all items larger than the first item.

    :param list: the list to be partitioned
    :param first: index of the first item
    :param last: index of the last item
    :return: Position of the item that splits the list into two partitions.
    """
    pivot_value = list[first]
    left_mark = first + 1
    right_mark = last

    done = False
    while not done:
        while left_mark <= right_mark and list[left_mark] <= pivot_value:
            left_mark = left_mark + 1

        while list[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark = right_mark - 1

        if right_mark < left_mark:
            done = True
        else:
            temp = list[left_mark]
            list[left_mark] = list[right_mark]
            list[right_mark] = temp

    temp = list[first]
    list[first] = list[right_mark]
    list[right_mark] = temp

    return right_mark

def calculate_name_score(name, index):
    """
    Calculate scores for name at a certain index, with rule A = 1, B = 2, etc., then multiply by index to get final score
    :param name: the name to calculate score
    :param index: index of that name
    :return: the score of the name at that index
    """
    score = 0
    # Loop through all letters in 'name' and convert their corresponding ASCII numbers to numbers from 1 to 26
    for c in name:
        score += ord(c) - 64

    return score * index

def main():
    # Trying bubble sort
    start_time = time.time()
    total_score = 0
    bubble_sort_name_list = read_data_from_file('project_euler_22.txt')
    bubble_sort_names(bubble_sort_name_list)

    for name in bubble_sort_name_list:
        total_score += calculate_name_score(name, bubble_sort_name_list.index(name) + 1)

    elapsed = time.time() - start_time

    print("Bubble sort: {0} found in {1} seconds".format(total_score, elapsed))

    # Trying quick sort
    start_time = time.time()
    total_score = 0
    quick_sort_name_list = read_data_from_file('project_euler_22.txt')
    quick_sort_names(quick_sort_name_list)

    for name in quick_sort_name_list:
        total_score += calculate_name_score(name, quick_sort_name_list.index(name) + 1)

    elapsed = time.time() - start_time

    print("Quick sort: {0} found in {1} seconds".format(total_score, elapsed))


if __name__ == "__main__":
    main()