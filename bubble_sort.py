def bubble_sort(data_list):
    n = len(data_list)
    for i in range(0, n):
        for j in range(0, n-i-1):
            if data_list[j] > data_list[j+1]:
                temp = data_list[j]
                data_list[j] = data_list[j+1]
                data_list[j+1] = temp


if __name__ == '__main__':
    data_list = [8, 15, 3, 5, 2, 20, 10, 1]
    bubble_sort(data_list)
    print('Bubble Sorted List:', data_list)
