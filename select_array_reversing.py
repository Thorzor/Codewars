def sel_reverse(arr, l):
    new_arr = []

    if l > len(arr):
        arr.reverse()
        return arr

    if l == 0:
        return arr

    while True:
        if len(arr) != 0:

            if l >= len(arr):
                counter = len(arr)
            else:
                counter = l

            values = []
            count = counter

            for i in range(counter):
                values.append(arr[i])
                counter -= 1

            values.reverse()

            for y in values:
                new_arr.append(y)

            for x in range(count):
                arr.pop(0)

        else:
            break
    return new_arr