def bubble_sort(data_list):
    n = len(data_list)
    for i in range(0, n):
        print("i = ", i)
        for j in range(0, n-i-1):
            print("j = ", j)
            if data_list[j] > data_list[j+1]:
                temp = data_list[j]
                data_list[j] = data_list[j+1]
                data_list[j+1] = temp
        if data_list[n-1] > data_list[n-2]:
            break


if __name__ == '__main__':
    data_list = [1, 2, 3, 4, 5, 7, 6]
    bubble_sort(data_list)
    print('Bubble Sorted List:', data_list)
